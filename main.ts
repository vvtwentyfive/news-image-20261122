// THE SUNDAY WORLD — news-image-20261122 entrypoint (Node 22, stdlib only).
// The front page is drawn by render.py at build time and ships beside this
// file as entry.png; this program places it at /output/entry.png for the
// grader. No network, no clock, no randomness: two runs are byte-identical.
import { chmodSync, copyFileSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
const src = join(dirname(fileURLToPath(import.meta.url)), 'entry.png');
const dst = join(outDir, 'entry.png');
copyFileSync(src, dst);
chmodSync(dst, 0o644);
