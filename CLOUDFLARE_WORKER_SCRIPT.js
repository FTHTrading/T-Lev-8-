// T-LEV-8 Legacy Domain Redirect Worker
// Deploy to Cloudflare Workers, map custom domains

const redirects = {
  'troptionsxchange.io': 'https://troptionslive.unykorn.org/exchange-os',
  'www.troptionsxchange.io': 'https://troptionslive.unykorn.org/exchange-os',
  'troptions-university.com': 'https://fthedu.unykorn.org/',
  'www.troptions-university.com': 'https://fthedu.unykorn.org/',
  'troptionstelevisionnetwork.tv': 'https://troptionslive.unykorn.org/sports',
  'www.troptionstelevisionnetwork.tv': 'https://troptionslive.unykorn.org/sports',
  'hotrcw.com': 'https://troptionslive.unykorn.org/',
  'www.hotrcw.com': 'https://troptionslive.unykorn.org/',
  'therealestateconnections.com': 'https://aurora.unykorn.org/',
  'www.therealestateconnections.com': 'https://aurora.unykorn.org/',
  'green-n-go.solar': 'https://impact.unykorn.org/',
  'www.green-n-go.solar': 'https://impact.unykorn.org/',
};

export default {
  async fetch(request) {
    const url = new URL(request.url);
    const target = redirects[url.hostname.toLowerCase()];
    
    if (target) {
      return Response.redirect(target, 301);
    }
    
    return new Response('Not found', { status: 404 });
  }
};
