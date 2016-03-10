--TEST--
void stream_bucket_prepend ( resource $brigade , object $bucket );
--CREDITS--
marcosptf - <marcosptf@yahoo.com.br> - #phparty7 - @phpsp - novatec/2015 - sao paulo - br
--SKIPIF--
<?php
if (phpversion() < "5.3.0") {
  die('SKIP php version so lower.');
}
?>
--FILE--
<?php
class foo extends php_user_filter {
<<<<<<< HEAD

  protected $calls = 0;
  
  public function filter($in, $out, &$consumed, $closing) {
  
    while ($bucket = stream_bucket_make_writeable($in)) {
      $consumed += $bucket->datalen;
      if ($this->calls++ == 2) {
   
=======
  protected $calls = 0;
  public function filter($in, $out, &$consumed, $closing) {
    while ($bucket = stream_bucket_make_writeable($in)) {
      $consumed += $bucket->datalen;
      if ($this->calls++ == 2) {
        // This bucket will appear again before any other bucket.
>>>>>>> 55ce793816ac7cea49b111562491e38863c07824
        stream_bucket_prepend($in, $bucket);
      }
    }
    return PSFS_FEED_ME;
  }
}
<<<<<<< HEAD

stream_filter_register('test', 'foo');
print  file_get_contents('http://yahoo.com/read=test/resource=foo');
?>
--EXPECT--
=======
stream_filter_register('test', 'foo');
print  file_get_contents('php://filter/read=test/resource=foo');
?>
--EXPECT--
>>>>>>> 55ce793816ac7cea49b111562491e38863c07824
