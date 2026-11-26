// Entry program for make.fun's "Promote make.fun's make-your-own-bounty
// post on X" bounty (program/v1, Node 22, standard library only).
//
// The post itself is the entry: one post of your own on X that quotes
// make.fun's make-your-own-bounty post
// (https://x.com/makefunai/status/2124915864336236646) or links to it,
// with a photo of its own attached, make.fun or the @makefunai tag and
// your play code in its text. This program does nothing but hand the
// post's address in: it reads POST.json from the repository root and
// writes it to the output directory, where the gate reads it. The
// house then reads the post's replies, reposts and quotes from X;
// the score is replies + reposts + quotes. Views and likes move
// nothing, and nothing this program writes about the post is scored.
//
// POST.json still holds the placeholder address until the post is
// published on X; replace it with the real post address
// ({"url": "https://x.com/<handle>/status/<id>"}) before submitting.
//
// Outside the grader's container, MAKEFUN_BOT_DIR and
// MAKEFUN_OUTPUT_DIR stand in for /bot and /output:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

const source = join(BOT_DIR, 'POST.json');
const target = join(OUTPUT_DIR, 'POST.json');

let raw: string;
try {
  raw = readFileSync(source, 'utf8');
} catch (err) {
  console.error(`POST.json could not be read from ${BOT_DIR}: ${(err as Error).message}`);
  process.exit(1);
}

let parsed: unknown;
try {
  parsed = JSON.parse(raw);
} catch (err) {
  console.error(`POST.json is not valid JSON: ${(err as Error).message}`);
  process.exit(1);
}

if (typeof parsed !== 'object' || parsed === null || typeof (parsed as { url?: unknown }).url !== 'string') {
  console.error('POST.json must be an object with a string "url" field');
  process.exit(1);
}

mkdirSync(OUTPUT_DIR, { recursive: true });
writeFileSync(target, JSON.stringify(parsed) + '\n', 'utf8');
console.log(`Wrote ${target}: ${(parsed as { url: string }).url}`);
