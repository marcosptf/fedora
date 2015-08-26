<?php
/**
 * 
 * @property Zend_Controller_Front $frontController
 */
class ListaclientesControllerTest extends Zend_Test_PHPUnit_ControllerTestCase
{


    public function setUp()
    {
        $this->bootstrap = array($this, 'appBootstrap');
        parent::setUp();
        $_SERVER['HTTP_USER_AGENT'] = 'lero';
    }
    

    public function appBootstrap()
    {
        $this->frontController->setControllerDirectory(APPLICATION_PATH . '/controllers');
        
        require_once(APPLICATION_PATH . '/plugins/Translate.php');
        require_once(APPLICATION_PATH . '/plugins/Seguranca.php');
        require_once(APPLICATION_PATH . '/plugins/View.php');
        
        $this->frontController->registerPlugin(new Translate());
        $this->frontController->registerPlugin(new Tss_Seguranca_Plugin());
        $this->frontController->registerPlugin(new Tss_View_Plugin());
        $this->frontController->setControllerDirectory(APPLICATION_PATH . '/controllers');
        $this->frontController->setParam('env', APPLICATION_ENVIRONMENT);
                
        Zend_Layout::startMvc(APPLICATION_PATH . '/layouts/scripts');
        
        $view = Zend_Layout::getMvcInstance()->getView();
        $view->doctype('XHTML1_STRICT');
    }

    
    public function testChamadaAoTokenDeveRedirecionarParaIdiomas()
    {
        $postData = array(
            'n_fone' => '987654321',
        );
        
        $session = $this->getMockBuilder('Zend_Session_Namespace')->disableOriginalConstructor()
            ->getMock();
        $session->expects($this->any())->method('__get')
            ->will($this->returnCallback('sessionGetter'));
        $session->expects($this->any())->method('foo')
            ->will($this->returnValue('bar'));

        $this->getRequest()
            ->setMethod('POST')
            ->setPost($postData);
        
        $this->markTestIncomplete('falta mockar o request http e fazer o mock da session funcionar');
        $this->dispatch('/listaclientes/token');

        $lero = new Zend_Session_Namespace('Zend_Auth');
        $this->assertController('listaclientes');
        $this->assertAction('token');
        $this->assertResponseCode(302);
    }

    
}


function sessionGetter($classPropertyName)
{
    print($classPropertyName);
    switch ($classPropertyName) {
        case 'perfil':
            return 6;

        case 'login':
            return 'supercow';
    }
}
