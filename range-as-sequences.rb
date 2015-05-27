class VU

  include Comparable

  attr :volume

  def initialize(volume)
    @volume = volume
  end 

  def inspect
    '#' *  @volume
  end 

  def <=> (other)
    self.volume <=> other.volume
  end 

  def succ
    raise(IndexError, "volume too big") if @volume >= 9
    VU.new(@volume.succ)
  end 

end

medium = VU.new(4)
puts(medium.to_s)
#mediun.include ?(puts(VU.new(3)))


