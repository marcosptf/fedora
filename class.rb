
class Song
 
  def initialize(name,artist,duration)
    @name     = name
    @artist   = artist
    @duration = duration
  end 

  def to_s
    "Song: #{@name} - #{@artist} (#{@duration})"
  end 

end

aSong = Song.new("bicylops","fleck",250)
puts(aSong.inspect)
puts(aSong.to_s)


class KaraokeSong < Song
  def initialize(name, artist, duration, lyrics)
    super(name,artist,duration)
    @lyrics = lyrics
  end 

  def to_s
    super + " [#{@lyrics}]"    
  end 

end

bSong = KaraokeSong.new("My Way", "Sinatra",225, "and now the ...")
puts(bSong.to_s)


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


class Song
  def duration=(newDuration)
    @duration = newDuration
  end
end

dSong = Song.new("fedora","fickr","775")
puts("showing attribute duration before set=>"+dSong.duration)
dSong.duration = "969"
puts("showing attribute duration after set=>"+dSong.duration)


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


