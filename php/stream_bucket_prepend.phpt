--TEST--
void stream_bucket_prepend ( resource $brigade , object $bucket );
--CREDITS--
marcosptf - <marcosptf@yahoo.com.br> - @phpsp - sao paulo - br
--SKIPIF--
<?php
if (phpversion() < "5.3.0") {
  die('SKIP php version so lower.');
}
?>
--FILE--
<?php
class foo extends php_user_filter {

  protected $calls = 0;
  
  public function filter($in, $out, &$consumed, $closing) {
  
    while ($bucket = stream_bucket_make_writeable($in)) {
      $consumed += $bucket->datalen;
      if ($this->calls++ == 2) {

        stream_bucket_prepend($in, $bucket);
      }
    }
    return PSFS_FEED_ME;
  }
}

stream_filter_register('test', 'foo');
print  file_get_contents('http://yahoo.com/read=test/resource=foo');
?>
--EXPECT--