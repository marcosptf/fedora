
#class to log, this class can provide many 
#instances with the same constructor

class Logger
  private_class_method :new
  @@logger = nil 
 
  def Logger.create
    @@logger = new unless @@logger
    @@logger
  end 
end

puts(Logger.create)
puts(Logger.create)
puts(Logger.create)
#puts(Logger.create.id)
#puts(Logger.create.id)

