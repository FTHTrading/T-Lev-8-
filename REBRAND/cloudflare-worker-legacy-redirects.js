/**
 * Cloudflare Worker — legacy domain redirects (Free plan friendly).
 * Deploy: Workers & Pages → Create Worker → paste → add routes per host.
 *
 * Routes to attach (one route per zone or use Bulk Redirects on paid plans):
 *   troptionsxchange.io/*
 *   troptions-university.com/*
 *   troptionstelevisionnetwork.tv/*
 *   hotrcw.com/*
 *   troptions.io/*
 */

const REDIRECTS = {
  "troptionsxchange.io": "https://troptionslive.unykorn.org/exchange-os",
  "www.troptionsxchange.io": "https://troptionslive.unykorn.org/exchange-os",
  "troptions-university.com": "https://fthedu.unykorn.org/",
  "www.troptions-university.com": "https://fthedu.unykorn.org/",
  "troptionstelevisionnetwork.tv": "https://troptionslive.unykorn.org/sports",
  "www.troptionstelevisionnetwork.tv": "https://troptionslive.unykorn.org/sports",
  "hotrcw.com": "https://troptionslive.unykorn.org/",
  "www.hotrcw.com": "https://troptionslive.unykorn.org/",
  "troptions.io": "https://troptions.unykorn.org/troptions",
  "www.troptions.io": "https://troptions.unykorn.org/troptions",
};

export default {
  async fetch(request) {
    const host = new URL(request.url).hostname.toLowerCase();
    const target = REDIRECTS[host];
    if (target) {
      return Response.redirect(target, 301);
    }
    return new Response("Not configured", { status: 404 });
  },
};
