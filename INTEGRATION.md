# T-VEX-8 ↔ needai.unykorn.org Integration

## Option A: Iframe Embed (Easiest — 5 minutes)

Add to your `needai/app/deal-center/page.tsx`:

```tsx
// Add inside your DealCenter component
<div className="mt-8 border rounded-lg overflow-hidden">
  <iframe
    src="https://fthtrading.github.io/T-VEX-8-/"
    style={{ width: '100%', height: '800px', border: 'none' }}
    title="T-VEX-8 Deal Room"
    sandbox="allow-scripts allow-same-origin"
  />
</div>
```

## Option B: Full Next.js Integration (Better — 30 minutes)

Copy the HTML/CSS into your Next.js app:

1. **Create route:** `needai/app/T-VEX-8/page.tsx`
2. **Port the design:** Convert HTML to JSX components
3. **Connect to API:** Use your existing registry API for live data

Example component structure:
```tsx
// needai/app/T-VEX-8/page.tsx
import { LiquidGlassLayout } from '@/components/TVEX/LiquidGlassLayout';
import { ConditionsTracker } from '@/components/TVEX/ConditionsTracker';
import { KillSwitchTerminal } from '@/components/TVEX/KillSwitchTerminal';
import { IPFSVault } from '@/components/TVEX/IPFSVault';

export default function TVEXPage() {
  return (
    <LiquidGlassLayout>
      <ConditionsTracker conditions={conditionsData} />
      <KillSwitchTerminal />
      <IPFSVault documents={vaultData} />
    </LiquidGlassLayout>
  );
}
```

## Option C: Link Button (Simplest — 1 minute)

Just add a link in your existing DealCenter:

```tsx
<a
  href="https://fthtrading.github.io/T-VEX-8-/"
  target="_blank"
  rel="noopener noreferrer"
  className="inline-flex items-center gap-2 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
>
  <ExternalLink className="w-4 h-4" />
  Open T-VEX-8 Deal Room
</a>
```

---

## Recommended: Use BOTH

| Site | Purpose | Audience |
|------|---------|----------|
| **GitHub Pages** (`fthtrading.github.io`) | Public deal room, visual presentation | External parties, investors, regulators |
| **needai** (`needai.unykorn.org`) | Internal registry, live data, API-connected | Internal team, operations |

This gives you:
- ✅ Public transparency (GitHub)
- ✅ Internal operational control (needai)
- ✅ Redundancy if one goes down
- ✅ Different access levels (public vs private)

## Next Steps

1. ✅ Package built
2. ⏳ Push to GitHub
3. ⏳ Enable GitHub Actions Pages
4. ⏳ Verify site live
5. ⏳ Integrate with needai (choose Option A, B, or C)
