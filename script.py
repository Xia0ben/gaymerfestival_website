from xml.dom import minidom
import base64
from html.parser import HTMLParser

# Extract images in separate folder
def extract_images(xml_doc):
  images = xml_doc.getElementsByTagName('image')
  for counter, image in enumerate(images):
      data = image.getAttribute('xlink:href')
      if 'png' in data:
        formatstring = 'png'
        imgstring = data[22:]
      elif 'jpg' in data:
        formatstring = 'jpg'
        imgstring = data[22:]
      elif 'jpeg' in data:
        formatstring = 'jpg'
        imgstring = data[23:]
      imgdata = base64.b64decode(imgstring)
      relpath = f'images/{counter:02d}.{formatstring}'
      fullpath = '/home/xia0ben/Desktop/gaymerfestival_website/' + relpath
      with open(fullpath, 'wb') as f:
          f.write(imgdata)
      image.setAttribute('xlink:href', relpath)
    
# Add links to relevant elements
mail = "mailto:changerici@nextgaymer.com?body=Merci pour le contact ! Afin de lutter contre le spam, l'adresse mail affichée plus haut doit être modifiée en changeant le texte 'changerici' pour 'contact'. Au plaisir de recevoir votre mail."
homepage = 'index.html'
programmation = '#programme\ 2024'
twitch = 'https://www.twitch.tv/nextgaymeroff'
qui_sommes_nous = 'https://nextgaymer.com/qui-sommes-nous/'
evenements = 'https://nextgaymer.com/evenements/'
nous_rejoindre = 'https://nextgaymer.com/rejoignez-nous/'

id_to_link = {
  'logo-cote-ng': homepage,
  'Qui sommes nous': qui_sommes_nous,
  'Qui sommes nous_2': evenements,
  'Qui sommes nous_3': homepage,
  'Qui sommes nous_4': nous_rejoindre,
  'billeterie-button': '#billetterie',
  'twitch-button': twitch,
  'programmation-button': programmation,
  'programmation-button-2': programmation,
  'billet-1-jour-button': 'https://www.helloasso.com/associations/geeks-gamers-lgbt/evenements/entree-1j-gaymer-festival-2023',
  'billet-4-jours-button': 'https://www.helloasso.com/associations/geeks-gamers-lgbt/evenements/pass-4-jours-gaymer-festival-2023',
  'hebergement-button': 'https://www.helloasso.com/associations/geeks-gamers-lgbt/evenements/hebergement-gaymer-festival-2023',
  'hebergement-button-2': 'https://www.helloasso.com/associations/geeks-gamers-lgbt/evenements/hebergement-gaymer-festival-2023',
  'carte': 'https://goo.gl/maps/uyjuLGE6BorNsf9q7',
  'nous-contacter-button': mail,
  'twitch-button-2': twitch,
  'contact-button-2': mail,
  'programmation-button-3': programmation,
  'logo-sos-homophobie': 'https://www.sos-homophobie.org/',
  'logo-women-in-games': 'https://womeningamesfrance.org/',
  'logo-exit': 'https://sassqueer.fr/',
  'logo-enipse': 'https://www.enipse.fr/',
  'logo-soeurs': 'http://www.couventdes69gaules.fr/',
  'logo-representrans': 'https://representrans.fr/',
  'logo-arkane': 'https://www.arkane-studios.com/fr',
  'logo-ea': 'https://www.ea.com/fr-fr',
  'logo-ubisoft': 'https://www.ubisoft.com/fr-fr/',
  'faire-un-don-button': 'https://www.helloasso.com/associations/geeks-gamers-lgbt/adhesions/adhesion-a-l-association-2023',
  'nous-contacter-button-3': mail,
  'logo-ng': 'https://nextgaymer.com/',
  'footer-qui-sommes-nous': qui_sommes_nous,
  'footer-evenements': evenements,
  'footer-gaymer-festival': homepage,
  'footer-nous-rejoindre': nous_rejoindre,
  'footer-jouons-pour-sos-homophobie': 'https://nextgaymer.com/jouons-pour-sos-homophobie/',
  'footer-forum': 'https://nextgaymer.com/communaute/',
  'footer-discord': 'https://discord.gg/8P4UbXA',
  'footer-twitch': twitch,
  'footer-instagram': 'https://www.instagram.com/nextgaymer/',
  'footer-facebook': 'https://www.facebook.com/NextGaymer/',
  'footer-twitter': 'https://twitter.com/NextGaymer',
  'footer-youtube': 'https://www.youtube.com/c/NextGaymer',
  'footer-steam': 'http://steamcommunity.com/groups/NextGaymer',
  'footer-contact': mail,
  'footer-reglement-interieur': 'https://nextgaymer.com/reglement-interieur-de-lassociation/',
  'footer-statuts-de-l-association': 'https://nextgaymer.com/?page_id=8089&preview=true',
  'footer-loup-lacaille': 'https://www.behance.net/LACAILLE',
  'go-up-button': '#top'
}

text_to_id = {
  'QUI SOMMES NOUS ?': 'footer-qui-sommes-nous',
  'ÉVÉNEMENTS': 'footer-evenements',
  'NOUS REJOINDRE': 'footer-nous-rejoindre',
  '#JOUONSPOURSOSHOMOPHOBIE': 'footer-jouons-pour-sos-homophobie',
  'FORUM': 'footer-forum',
  'GAYMER FESTIVAL': 'footer-gaymer-festival',
  'DISCORD': 'footer-discord',
  'TWITCH': 'footer-twitch',
  'INSTAGRAM': 'footer-instagram',
  'FACEBOOK': 'footer-facebook',
  'TWITTER': 'footer-twitter',
  'YOUTUBE': 'footer-youtube',
  'STEAM': 'footer-steam',
  'FAQ': 'footer-faq',
  'CONTACT': 'footer-contact',
  'PRESSE': 'footer-presse',
  'RÈGLEMENT INTÉRIEUR': 'footer-reglement-interieur',
  'STATUTS DE L’ASSOCIATION': 'footer-statuts-de-l-association',
  'BUREAU ET BÉNÉVOLES': 'footer-bureau-et-benevoles',
  'POLITIQUE DE CONFIDENTIALITÉ': 'footer-politique-de-confidentialite',
  'CGU': 'footer-cgu',
  'POLITIQUE DE COOKIES': 'footer-politique-de-cookies',
  'MENTIONS LÉGALES': 'footer-mentions-legales',
  'BEHANCE.NET/LACAILLE': 'footer-loup-lacaille'
}

buttons_to_fill = [
  'twitch-button',
  'programmation-button',
  'programmation-button-2',
  'billet-1-jour-button',
  'hebergement-button',
  'hebergement-button-2',
  'nous-contacter-button',
  'twitch-button-2',
  'contact-button-2',
  'programmation-button-3',
  'nous-contacter-button-3',
  'go-up-button'
]

def set_all_id_attributes_as_ids(svg_doc):
    queue = [svg_doc]
    while queue:
        current = queue.pop()
        queue += current.childNodes
        if getattr(current, "hasAttribute", None) and current.hasAttribute('id'):
            current.setIdAttribute('id')

def add_links(svg_doc):
  # Add ids to footer link text elements
  footer = svg_doc.getElementById('footer')
  footer_tspans = footer.getElementsByTagName('tspan')
  for tspan in footer_tspans:
    text = tspan.firstChild.data.strip()
    if text in text_to_id:
      tspan.setAttribute('id', text_to_id[text])
      # Fix strange underline behavior in all browsers and placing in Firefox
      if tspan.parentNode.hasAttribute('xml:space'):
        tspan.parentNode.removeAttribute('xml:space')
      if tspan.parentNode.hasAttribute('style'):
        tspan.parentNode.removeAttribute('style')

  # Add links for everyone
  for key, value in id_to_link.items():
    svgElement = svg_doc.getElementById(key)
    if svgElement is not None:
      link = svg_doc.createElementNS("http://www.w3.org/2000/svg", "a")
      link.setAttributeNS('http://www.w3.org/1999/xlink', 'xlink:href', value)
      svgElement.appendChild(link)
      # for child in svgElement.childNodes:
      #   link.appendChild(child)

  # Fill background of button elements with transparent color to improve clicking
  for button_id in buttons_to_fill:
    button = svg_doc.getElementById(button_id)
    if button is not None:
      button.setAttribute('class', 'fill-button')

# if __name__ == '__main__':
filename = 'moon'
svg_filepath = f'/home/xia0ben/Desktop/{filename}.svg'

svg = minidom.parse(svg_filepath)
svg_out_filepath = f'/home/xia0ben/Desktop/{filename}_out.svg'

html_in_filepath = '/home/xia0ben/Desktop/gaymerfestival_website/index_in.html'
html_out_filepath = '/home/xia0ben/Desktop/gaymerfestival_website/index.html'

set_all_id_attributes_as_ids(svg)
extract_images(svg)

# add_links(svg)

svg.firstChild.removeAttribute('width')
svg.firstChild.removeAttribute('height')
svg.firstChild.setAttribute('viewBox', '4 4 1440 6372')

# with open(svg_out_filepath, 'w') as f:
#     svg.writexml(f)

html = ''
with open(html_in_filepath) as f:
  html = f.read()

out_html = html.replace('<main>\n', '<main>\n' + svg.toxml())

with open(html_out_filepath, 'w') as f:
    f.write(out_html)
