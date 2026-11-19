// gta6-meme-x-01 — "Leonida Ghost" meme entry.
//
// What this program does: the entry IS the X post named in POST.json, so this
// file only has to hand that file to the grader. It reads POST.json from the
// repository and writes an identical copy into the output directory. The meme
// picture and the post itself are already made; the house reads the post
// directly from X, so nothing written here is judged.
//
// Local run:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';

const repoDir = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

const srcPath = join(repoDir, 'POST.json');
const dstPath = join(outDir, 'POST.json');

let payload: string;
try {
  payload = readFileSync(srcPath, 'utf8');
} catch (err) {
  console.error(`failed to read ${srcPath}: ${(err as Error).message}`);
  process.exit(1);
}

// The entry is only valid if POST.json names a real X post address, so check
// the url before copying it: it must be an x.com or twitter.com status link.
let postUrl: unknown;
try {
  postUrl = JSON.parse(payload).url;
} catch (err) {
  console.error(`POST.json is not valid JSON: ${(err as Error).message}`);
  process.exit(1);
}
if (
  typeof postUrl !== 'string' ||
  !postUrl.startsWith('https://x.com/') &&
  !postUrl.startsWith('https://twitter.com/') ||
  !postUrl.includes('/status/')
) {
  console.error(
    `POST.json url must be an X post address (https://x.com/<handle>/status/<id>), got: ${String(postUrl)}`,
  );
  process.exit(1);
}

mkdirSync(outDir, { recursive: true });

try {
  writeFileSync(dstPath, payload);
} catch (err) {
  console.error(`failed to write ${dstPath}: ${(err as Error).message}`);
  process.exit(1);
}

console.log(`copied POST.json to ${dstPath}`);
