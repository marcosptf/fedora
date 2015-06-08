class Song
 
  #initialize method, is used to start instance of class
  #starting variables like this above
  def initialize(name,artist,duration)
    @name     = name
    @artist   = artist
    @duration = duration
  end 
  
  #the method to_s give output of message and variables in string way
  def to_s
    "Song: #{@name} - #{@artist} (#{@duration})"
  end 

end
aSong = Song.new("bicylops","fleck",250)
puts(aSong.inspect)
puts(aSong.to_s)




#this class is inharitence Song class
class KaraokeSong < Song

  def initialize(name, artist, duration, lyrics)
    #here super is reference the Song class that was inherited
    super(name,artist,duration)
    @lyrics = lyrics
  end 

  def to_s
    super + " [#{@lyrics}]"    
  end 
end
bSong = KaraokeSong.new("My Way", "Sinatra",225, "and now the ...")
puts(bSong.to_s)




#this class is used to after instance, to get values set after inicialized
class Song
  def name
    @name
  end 

  def artist
    @artist
  end 

  def duration
    @duration
  end 
end
cSong = Song.new("java","ruby","1234")
puts("name=>"+cSong.name)
puts("artist=>"+cSong.artist)
puts("duration=>"+cSong.duration)








#class that can be set duration by method 
class Song
  def duration=(newDuration)
    @duration = newDuration
  end
end
dSong = Song.new("fedora","fickr","775")
puts("showing attribute duration before set=>"+dSong.duration)
dSong.duration = "969"
puts("showing attribute duration after set=>"+dSong.duration)





#class that can be set duration in minutes
class Song
  def durationInMinutes
    @duration/60.0
  end

  def durationInMinutes=(value)
    @duration = (value*60).to_i
  end
end
eSong = Song.new("java scripter","java2",283)
puts(eSong.durationInMinutes)
eSong.durationInMinutes = 3.14
puts(eSong.duration)










#this class is used to show the diference between declare the
#variable @variable and @@variable
#@variable => called variable of instance, used in methods
#@@variable=> called vabiable of class, represent a object itself
class Song
  @@plays1 = 0

  def initialize(name,artist,duration)
    @name     = name
    @artist   = artist
    @duration = duration
    @plays    = 0
  end

  def play
    @plays   += 1
    @@plays1 += 1
    "This song: #@plays play. Total #@@plays1 plays"
  end
end
s1 = Song.new("Song1","artist1",234)
s2 = Song.new("Song2","artist2",456)
puts(s1.play)
puts(s2.play)
puts(s1.play)
puts(s2.play)







class SongList
  MaxTime = 5 * 60
  def SongList.isTooLong(aSong)
    return aSong.duration > MaxTime
  end
end
song1 = Song.new("java","flickr",123)
puts(SongList.isTooLong(song1))
song2 = Song.new("the calling","santana",468)
puts(SongList.isTooLong(song2))




