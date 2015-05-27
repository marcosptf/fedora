#many ways to use access control in methods

class Myclass

  def method1
    puts("method default (public)")
  end 

  protected
  def method2
    puts("method protected")
  end 
  
  private
  def method3
    puts("method private")
  end 

  public
  def method4
    puts("method public")
  end 

end


