 from collections import Sequence
 from magma import *
 from .LUT import LUT1, LUT2, LUT3, LUT4, LUT5, LUT6, LUT7, LUT8
+import __builtin__
 
 __all__  = ['ROM1', 'ROM2', 'ROM3', 'ROM4']
 __all__ += ['ROM5', 'ROM6', 'ROM7', 'ROM8']
@@ -102,6 +103,10 @@ def ROM(rom, **kwargs):
 
 ROMCache = {}
 
+# Rom Module name
+def _ROMName(name, n, data):
+    return '%s%d_%d' % (name, n, abs(hash(__builtin__.tuple(data))))
+
 def DefineROM16xN(rom):
     """
     Construct a 16 entry ROM of arbitrary width.
@@ -114,7 +119,7 @@ def DefineROM16xN(rom):
     n = len(rom)
 
     # could be different memory contents ...
-    name = _ROMName('ROM16x', n)
+    name = _ROMName('ROM16x', n, rom)
     if name in ROMCache:
         return ROMCache[name]
 
@@ -139,4 +144,4 @@ def DefineROM16xN(rom):
 # Create a 16xN ROM
 #
 def ROM16xN(rom):
-    return DefineROM16xN(rom)(**kwargs)
+    return DefineROM16xN(rom)()
