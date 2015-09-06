diff -r 4884af6d3e30 Lib/test/test_ssl.py
--- a/Lib/test/test_ssl.py	Sun Aug 16 23:22:32 2015 -0400
+++ b/Lib/test/test_ssl.py	Mon Aug 24 19:38:44 2015 -0300
@@ -713,13 +713,11 @@
 
     @skip_if_broken_ubuntu_ssl
     def test_options(self):
+
+        # test to ssl.PROTOCOL_TLSv1
         ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
-        # OP_ALL | OP_NO_SSLv2 is the default value
-        self.assertEqual(ssl.OP_ALL | ssl.OP_NO_SSLv2,
-                         ctx.options)
+        self.assertEqual(ssl.PROTOCOL_TLSv1, ctx.protocol)
         ctx.options |= ssl.OP_NO_SSLv3
-        self.assertEqual(ssl.OP_ALL | ssl.OP_NO_SSLv2 | ssl.OP_NO_SSLv3,
-                         ctx.options)
         if can_clear_options():
             ctx.options = (ctx.options & ~ssl.OP_NO_SSLv2) | ssl.OP_NO_TLSv1
             self.assertEqual(ssl.OP_ALL | ssl.OP_NO_TLSv1 | ssl.OP_NO_SSLv3,
@@ -730,6 +728,77 @@
             with self.assertRaises(ValueError):
                 ctx.options = 0
 
+        # test to ssl.PROTOCOL_TLSv1_1
+        ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_1)
+        self.assertEqual(ssl.PROTOCOL_TLSv1_1, ctx.protocol)
+        ctx.options |= ssl.OP_NO_SSLv3
+        if can_clear_options():
+            ctx.options = (ctx.options & ~ssl.OP_NO_SSLv2) | ssl.OP_NO_TLSv1
+            self.assertEqual(ssl.OP_ALL | ssl.OP_NO_TLSv1 | ssl.OP_NO_SSLv3,
+                             ctx.options)
+            ctx.options = 0
+            self.assertEqual(0, ctx.options)
+        else:
+            with self.assertRaises(ValueError):
+                ctx.options = 0
+
+        # test to ssl.PROTOCOL_TLSv1_2
+        ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
+        self.assertEqual(ssl.PROTOCOL_TLSv1_2, ctx.protocol)
+        ctx.options |= ssl.OP_NO_SSLv3
+        if can_clear_options():
+            ctx.options = (ctx.options & ~ssl.OP_NO_SSLv2) | ssl.OP_NO_TLSv1
+            self.assertEqual(ssl.OP_ALL | ssl.OP_NO_TLSv1 | ssl.OP_NO_SSLv3,
+                             ctx.options)
+            ctx.options = 0
+            self.assertEqual(0, ctx.options)
+        else:
+            with self.assertRaises(ValueError):
+                ctx.options = 0
+
+        # ssl.PROTOCOL_SSLv2
+        ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv2)
+        self.assertEqual(ssl.PROTOCOL_SSLv2, ctx.protocol)
+        ctx.options |= ssl.OP_NO_SSLv3
+        if can_clear_options():
+            ctx.options = (ctx.options & ~ssl.OP_NO_SSLv2) | ssl.OP_NO_TLSv1
+            self.assertEqual(ssl.OP_ALL | ssl.OP_NO_TLSv1 | ssl.OP_NO_SSLv3,
+                             ctx.options)
+            ctx.options = 0
+            self.assertEqual(0, ctx.options)
+        else:
+            with self.assertRaises(ValueError):
+                ctx.options = 0
+
+        # ssl.PROTOCOL_SSLv23
+        ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
+        self.assertEqual(ssl.PROTOCOL_SSLv23, ctx.protocol)
+        ctx.options |= ssl.OP_NO_SSLv3
+        if can_clear_options():
+            ctx.options = (ctx.options & ~ssl.OP_NO_SSLv2) | ssl.OP_NO_TLSv1
+            self.assertEqual(ssl.OP_ALL | ssl.OP_NO_TLSv1 | ssl.OP_NO_SSLv3,
+                             ctx.options)
+            ctx.options = 0
+            self.assertEqual(0, ctx.options)
+        else:
+            with self.assertRaises(ValueError):
+                ctx.options = 0
+
+        # ssl.PROTOCOL_SSLv3
+        ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv3)
+        self.assertEqual(ssl.PROTOCOL_SSLv3, ctx.protocol)
+        ctx.options |= ssl.OP_NO_SSLv3
+        if can_clear_options():
+            ctx.options = (ctx.options & ~ssl.OP_NO_SSLv2) | ssl.OP_NO_TLSv1
+            self.assertEqual(ssl.OP_ALL | ssl.OP_NO_TLSv1 | ssl.OP_NO_SSLv3,
+                             ctx.options)
+            ctx.options = 0
+            self.assertEqual(0, ctx.options)
+        else:
+            with self.assertRaises(ValueError):
+                ctx.options = 0
+
+
     def test_verify_mode(self):
         ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
         # Default value
