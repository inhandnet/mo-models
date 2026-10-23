import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
test('model compilation retains the documented calibration and unchanged official contract',()=>{
 const compile=fs.readFileSync('compile/zone-demo/compile_model.py','utf8');
 const model=fs.readFileSync('compile/zone-demo/model.py','utf8');
 assert.ok(compile.includes('REL.TIDL.11.02.17.00'));
 assert.ok(compile.includes("'advanced_options:calibration_frames': len(frames)"));
 assert.ok(model.includes('0..255 float RGB, not uint8 and not RGB/255'));
});
