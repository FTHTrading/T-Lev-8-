/**
 * Cloudflare Worker — TROPTIONS Legacy Domain Redirects
 * Routes: troptionsxchange.io, troptions-university.com,
 *         troptionstelevisionnetwork.tv, hotrcw.com, troptions.io
 * Status: 301 Permanent
 *
 * Deploy: Workers & Pages → Create Worker → paste → Triggers → Custom Domains (apex + www)
 * SSL/TLS: Full (strict) on each zone
 */
const REDIRECT_MAP = {
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
    const url = new URL(request.url);
    const target = REDIRECT_MAP[url.hostname];

    if (target) {
      return Response.redirect(target, 301);
    }

    return new Response("Domain not configured. Contact TROPTIONS support.", {
      status: 404,
      headers: { "Content-Type": "text/plain" },
    });
  },
};
