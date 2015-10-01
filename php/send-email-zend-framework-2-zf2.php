<?php
namespace User\Service;
use User\Entity\User;
use Zend\Mime\Part;
use Zend\Mime\Message;
use Zend\Mail;
use Zend\Mail\Transport\Sendmail as SendmailTransport;
class SendMailService
{
private $viewRenderer;
private $template;
private $content;
public function __construct($viewRenderer)
{
$this->viewRenderer = $viewRenderer;
}
public function setTemplate($name)
{
if (empty($name))
throw new \InvalidArgumentException("Template name can not be empty");
$this->template = $name;
}
public function getTemplate()
{
return $this->template;
}
/**
* TODO Implement Token Generate
*/
public function setContentData(User $user)
{
$content = $this->viewRenderer->render(
$this->getTemplate(),
[
'name' => $user->getDisplayName(),
'id' => $user->getId(),
'login' => $user->getUsername(),
'token' => '90909'
]
);
$this->content = new Part($content);
$this->content->type = "text/html";
}
/**
* TODO break their responsibilities
*/
public function send($mailTo)
{
$body = new Message();
$body->setParts([$this->content, ]);
$message = new Mail\Message();
$message->addTo($mailTo)
->addFrom('contato@doletaz.com.br')
->setSubject('Bem Vindo ao Doletaz!')
->setBody($body);
$transport = new SendmailTransport();
$transport->send($message);
}
}
