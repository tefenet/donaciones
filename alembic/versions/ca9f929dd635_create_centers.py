"""create centers

Revision ID: ca9f929dd635
Revises: 6b6bd5f86431
Create Date: 2020-10-22 19:20:54.757635

"""
from datetime import datetime

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
from sqlalchemy import ForeignKey

revision = 'ca9f929dd635'
down_revision = '6b6bd5f86431'
branch_labels = None
depends_on = None


def upgrade():
    city_table = op.create_table(
        'city',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(100), nullable=False),
    )
    type_table = op.create_table(
        'centerType',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('description', sa.String(100), nullable=False),
    )
    centers_table = op.create_table(
        'centers',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('email', sa.String(100), nullable=False, unique=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('address', sa.String(100), nullable=True),
        sa.Column('phone', sa.String(100)),
        sa.Column('web_site', sa.String(100)),
        sa.Column('published', sa.Boolean(), default=False),
        sa.Column('geo_location', sa.String(100)),
        sa.Column('opening', sa.Time()),
        sa.Column('closing', sa.Time()),
        sa.Column('protocol', sa.LargeBinary()),
        sa.Column('city_id', sa.Integer, ForeignKey('city.id')),
        sa.Column('type_id', sa.Integer, ForeignKey('centerType.id')),
    )

    op.bulk_insert(city_table,
                   [
                       {
                           "name": "Bengkulu"
                       },
                       {
                           "name": "Duluth"
                       },
                       {
                           "name": "Brescia"
                       },
                       {
                           "name": "Daknam"
                       },
                       {
                           "name": "Argyle"
                       },
                       {
                           "name": "Bensheim"
                       },
                       {
                           "name": "Santa Coloma de Gramenet"
                       },
                       {
                           "name": "Killa Saifullah"
                       },
                       {
                           "name": "Serralunga d'Alba"
                       },
                       {
                           "name": "Puno"
                       },
                       {
                           "name": "Hertsberge"
                       },
                       {
                           "name": "Pictou"
                       },
                       {
                           "name": "Neerharen"
                       },
                       {
                           "name": "Talagante"
                       },
                       {
                           "name": "Patna"
                       },
                       {
                           "name": "Akron"
                       },
                       {
                           "name": "Grande Prairie"
                       },
                       {
                           "name": "Thunder Bay"
                       },
                       {
                           "name": "Thirimont"
                       },
                       {
                           "name": "Tavier"
                       },
                       {
                           "name": "Hartlepool"
                       },
                       {
                           "name": "Anápolis"
                       },
                       {
                           "name": "Pulderbos"
                       },
                       {
                           "name": "Robelmont"
                       },
                       {
                           "name": "Desteldonk"
                       },
                       {
                           "name": "Grand Falls"
                       },
                       {
                           "name": "Harrisburg"
                       },
                       {
                           "name": "Trinità d'Agultu e Vignola"
                       },
                       {
                           "name": "Toledo"
                       },
                       {
                           "name": "Alva"
                       },
                       {
                           "name": "Independence"
                       },
                       {
                           "name": "Magdeburg"
                       },
                       {
                           "name": "Beausejour"
                       },
                       {
                           "name": "Burlington"
                       },
                       {
                           "name": "Uruapan"
                       },
                       {
                           "name": "Bergen op Zoom"
                       },
                       {
                           "name": "Zelzate"
                       },
                       {
                           "name": "Lochristi"
                       },
                       {
                           "name": "Centa San Nicolò"
                       },
                       {
                           "name": "Montebelluna"
                       },
                       {
                           "name": "West Jakarta"
                       },
                       {
                           "name": "Rosoux-Crenwick"
                       },
                       {
                           "name": "Valéncia"
                       },
                       {
                           "name": "Bischofshofen"
                       },
                       {
                           "name": "Scarborough"
                       },
                       {
                           "name": "San Miguel"
                       },
                       {
                           "name": "Jaén"
                       },
                       {
                           "name": "Cabras"
                       },
                       {
                           "name": "Korba"
                       },
                       {
                           "name": "Veenendaal"
                       },
                       {
                           "name": "Neeroeteren"
                       },
                       {
                           "name": "Rostock"
                       },
                       {
                           "name": "Vietri di Potenza"
                       },
                       {
                           "name": "Punitaqui"
                       },
                       {
                           "name": "Curarrehue"
                       },
                       {
                           "name": "Conca Casale"
                       },
                       {
                           "name": "Baarle-Hertog"
                       },
                       {
                           "name": "Seilles"
                       },
                       {
                           "name": "Pocatello"
                       },
                       {
                           "name": "Joliet"
                       },
                       {
                           "name": "Agustín Codazzi"
                       },
                       {
                           "name": "Lodine"
                       },
                       {
                           "name": "Querétaro"
                       },
                       {
                           "name": "Chépica"
                       },
                       {
                           "name": "Wagga Wagga"
                       },
                       {
                           "name": "Oostmalle"
                       },
                       {
                           "name": "Sousa"
                       },
                       {
                           "name": "Naarden"
                       },
                       {
                           "name": "Anjou"
                       },
                       {
                           "name": "Värnamo"
                       },
                       {
                           "name": "Coleville Lake"
                       },
                       {
                           "name": "Weesp"
                       },
                       {
                           "name": "Panjgur"
                       },
                       {
                           "name": "Trani"
                       },
                       {
                           "name": "Sant'Angelo in Pontano"
                       },
                       {
                           "name": "Exeter"
                       },
                       {
                           "name": "Diegem"
                       },
                       {
                           "name": "Adelaide"
                       },
                       {
                           "name": "Lidingo"
                       },
                       {
                           "name": "West Valley City"
                       }
                   ])
    op.bulk_insert(type_table,
                   [
                       {
                           'description': 'ropa',
                       },
                       {
                           'description': 'comida',
                       }

                   ])
    op.bulk_insert(
                   centers_table,
        [
            {
                "name": "suscipit nonummy.",
                "address": "P.O. Box 806, 4278 Aliquam Avenue",
                "phone": "0764119719",
                "email": "Duis@aliquet.co.uk",
                "web_site": "www.Portia.com",
                "published": False,
                "city_id": 6,
                "type_id": 2,
                "opening": "04:06:07",
                "closing": "03:01:09",
                "geo_location": "-31.29486, 50.2512"
            },
            {
                "name": "Nullam velit",
                "address": "8790 At Street",
                "phone": "0417828796",
                "email": "quis@Quisquenonummyipsum.ca",
                "web_site": "www.Ebony.com",
                "published": True,
                "city_id": 2,
                "type_id": 1,
                "opening": "04:08:04",
                "closing": "07:07:00",
                "geo_location": "85.83742, -103.76786"
            },
            {
                "name": "Mauris vel",
                "address": "Ap #221-6501 Parturient Road",
                "phone": "0623680920",
                "email": "ligula@amagna.ca",
                "web_site": "www.Joan.com",
                "published": False,
                "city_id": 4,
                "type_id": 2,
                "opening": "01:06:04",
                "closing": "01:02:07",
                "geo_location": "-82.79091, 142.54743"
            },
            {
                "name": "Morbi accumsan",
                "address": "570-4117 Ut Ave",
                "phone": "0695870175",
                "email": "penatibus.et@Donecconsectetuer.com",
                "web_site": "www.Nell.com",
                "published": False,
                "city_id": 2,
                "type_id": 1,
                "opening": "04:03:03",
                "closing": "04:05:00",
                "geo_location": "74.7103, 39.4392"
            },
            {
                "name": "Nullam enim.",
                "address": "Ap #242-2089 Maecenas St.",
                "phone": "0219943833",
                "email": "Vivamus@blanditviverraDonec.org",
                "web_site": "www.Jessica.com",
                "published": True,
                "city_id": 12,
                "type_id": 2,
                "opening": "06:08:03",
                "closing": "00:04:07",
                "geo_location": "45.39751, -179.16994"
            },
            {
                "name": "tincidunt vehicula",
                "address": "649-8038 Non Ave",
                "phone": "0908639751",
                "email": "aliquet.lobortis@velit.ca",
                "web_site": "www.Kirestin.com",
                "published": False,
                "city_id": 6,
                "type_id": 2,
                "opening": "09:09:09",
                "closing": "07:02:04",
                "geo_location": "-59.46329, -155.42096"
            },
            {
                "name": "auctor, nunc",
                "address": "8985 Cum St.",
                "phone": "0305192876",
                "email": "posuere@rhoncusNullam.ca",
                "web_site": "www.Alisa.com",
                "published": False,
                "city_id": 5,
                "type_id": 1,
                "opening": "03:04:04",
                "closing": "05:06:00",
                "geo_location": "-83.80931, -91.04102"
            },
            {
                "name": "dui. Fusce",
                "address": "Ap #479-3375 Neque Road",
                "phone": "0868239043",
                "email": "mauris.rhoncus.id@pellentesqueegetdictum.com",
                "web_site": "www.Karina.com",
                "published": True,
                "city_id": 13,
                "type_id": 2,
                "opening": "04:04:02",
                "closing": "05:06:00",
                "geo_location": "-33.27935, 77.08048"
            },
            {
                "name": "amet ultricies",
                "address": "P.O. Box 587, 1682 In Av.",
                "phone": "0344983713",
                "email": "in@ametconsectetuer.edu",
                "web_site": "www.Lynn.com",
                "published": False,
                "city_id": 13,
                "type_id": 2,
                "opening": "04:08:08",
                "closing": "01:07:02",
                "geo_location": "80.77438, -121.37416"
            },
            {
                "name": "blandit at,",
                "address": "3012 Nisl. Avenue",
                "phone": "0365483752",
                "email": "Nunc.mauris@aliquet.com",
                "web_site": "www.Charde.com",
                "published": True,
                "city_id": 7,
                "type_id": 1,
                "opening": "06:05:02",
                "closing": "08:01:09",
                "geo_location": "8.09866, 95.08471"
            },
            {
                "name": "Vestibulum ut",
                "address": "Ap #558-6288 Magna Rd.",
                "phone": "0900766919",
                "email": "vulputate.nisi@Duis.co.uk",
                "web_site": "www.Rachel.com",
                "published": True,
                "city_id": 6,
                "type_id": 1,
                "opening": "04:04:03",
                "closing": "02:07:05",
                "geo_location": "32.55042, 85.52072"
            },
            {
                "name": "Nam porttitor",
                "address": "P.O. Box 198, 3049 In Rd.",
                "phone": "0105163791",
                "email": "nec.urna.suscipit@sed.org",
                "web_site": "www.Fallon.com",
                "published": False,
                "city_id": 2,
                "type_id": 1,
                "opening": "02:01:01",
                "closing": "05:04:08",
                "geo_location": "43.2065, -140.65652"
            },
            {
                "name": "orci, adipiscing",
                "address": "Ap #669-1818 Est Street",
                "phone": "0380826735",
                "email": "sociis.natoque@sitametorci.co.uk",
                "web_site": "www.Hope.com",
                "published": False,
                "city_id": 16,
                "type_id": 1,
                "opening": "07:04:06",
                "closing": "04:00:06",
                "geo_location": "5.32367, 31.29493"
            },
            {
                "name": "semper et,",
                "address": "136-5023 Eu Av.",
                "phone": "0490728435",
                "email": "tincidunt@ategestas.org",
                "web_site": "www.Bryar.com",
                "published": True,
                "city_id": 18,
                "type_id": 2,
                "opening": "04:01:06",
                "closing": "03:07:09",
                "geo_location": "-68.65469, -41.28149"
            },
            {
                "name": "sociosqu ad",
                "address": "Ap #454-7281 Leo Av.",
                "phone": "0977850236",
                "email": "id.enim@est.net",
                "web_site": "www.Justina.com",
                "published": False,
                "city_id": 4,
                "type_id": 1,
                "opening": "02:09:08",
                "closing": "07:03:06",
                "geo_location": "61.89632, 72.3067"
            },
            {
                "name": "sociis natoque",
                "address": "439-3665 Nunc Avenue",
                "phone": "0443524809",
                "email": "Maecenas.malesuada.fringilla@sapienNunc.co.uk",
                "web_site": "www.Keelie.com",
                "published": True,
                "city_id": 3,
                "type_id": 1,
                "opening": "01:01:02",
                "closing": "00:00:03",
                "geo_location": "56.81126, -37.77715"
            },
            {
                "name": "condimentum. Donec",
                "address": "924-1599 In Rd.",
                "phone": "0429569212",
                "email": "Mauris.eu.turpis@nunc.co.uk",
                "web_site": "www.Orla.com",
                "published": True,
                "city_id": 3,
                "type_id": 2,
                "opening": "08:07:09",
                "closing": "05:01:00",
                "geo_location": "-16.62304, -36.20549"
            },
            {
                "name": "molestie in,",
                "address": "P.O. Box 300, 5050 Sed Road",
                "phone": "0185651055",
                "email": "purus@tincidunt.net",
                "web_site": "www.Chantale.com",
                "published": True,
                "city_id": 5,
                "type_id": 1,
                "opening": "09:01:01",
                "closing": "07:04:02",
                "geo_location": "42.31849, 148.69582"
            },
            {
                "name": "egestas. Fusce",
                "address": "5113 Semper Av.",
                "phone": "0177492277",
                "email": "in.felis.Nulla@mauris.net",
                "web_site": "www.Rebecca.com",
                "published": True,
                "city_id": 19,
                "type_id": 2,
                "opening": "09:09:08",
                "closing": "06:06:04",
                "geo_location": "40.099, -42.96511"
            },
            {
                "name": "lobortis risus.",
                "address": "P.O. Box 718, 7609 Pede. Ave",
                "phone": "0901330386",
                "email": "at.pede@lobortisquis.ca",
                "web_site": "www.Mollie.com",
                "published": True,
                "city_id": 19,
                "type_id": 2,
                "opening": "03:05:02",
                "closing": "09:03:09",
                "geo_location": "28.41873, 22.55746"
            },
            {
                "name": "ipsum primis",
                "address": "261-7862 Ipsum. Rd.",
                "phone": "0265624404",
                "email": "eget.tincidunt.dui@penatibuset.edu",
                "web_site": "www.Iona.com",
                "published": False,
                "city_id": 6,
                "type_id": 2,
                "opening": "05:01:03",
                "closing": "09:03:03",
                "geo_location": "70.59882, -0.67088"
            },
            {
                "name": "rhoncus id,",
                "address": "473-1216 Ultrices Rd.",
                "phone": "0278745725",
                "email": "semper.et.lacinia@mienim.ca",
                "web_site": "www.Ingrid.com",
                "published": True,
                "city_id": 10,
                "type_id": 1,
                "opening": "05:02:06",
                "closing": "00:02:01",
                "geo_location": "25.86124, 96.53659"
            },
            {
                "name": "dictum ultricies",
                "address": "890-4843 Dapibus Street",
                "phone": "0691200172",
                "email": "diam.Duis@egestasFusce.net",
                "web_site": "www.Hilda.com",
                "published": False,
                "city_id": 8,
                "type_id": 2,
                "opening": "07:06:01",
                "closing": "02:07:05",
                "geo_location": "20.89838, 167.99479"
            },
            {
                "name": "ultricies ligula.",
                "address": "P.O. Box 609, 1345 Elit, Avenue",
                "phone": "0843797200",
                "email": "mauris@sit.ca",
                "web_site": "www.Heidi.com",
                "published": True,
                "city_id": 12,
                "type_id": 1,
                "opening": "00:07:02",
                "closing": "03:07:04",
                "geo_location": "54.3232, 47.75695"
            },
            {
                "name": "ac turpis",
                "address": "6385 Suspendisse Rd.",
                "phone": "0561777760",
                "email": "Aenean.eget.magna@Nuncut.edu",
                "web_site": "www.Mia.com",
                "published": True,
                "city_id": 2,
                "type_id": 2,
                "opening": "09:05:09",
                "closing": "05:03:02",
                "geo_location": "-29.64639, -134.97268"
            },
            {
                "name": "mollis. Duis",
                "address": "196-2201 Duis St.",
                "phone": "0940926597",
                "email": "mollis.vitae@IntegerurnaVivamus.net",
                "web_site": "www.Beverly.com",
                "published": True,
                "city_id": 2,
                "type_id": 2,
                "opening": "07:01:02",
                "closing": "07:04:09",
                "geo_location": "48.90065, -72.63105"
            },
            {
                "name": "Nunc lectus",
                "address": "9196 Orci St.",
                "phone": "0458234758",
                "email": "sociis.natoque@Integertincidunt.com",
                "web_site": "www.Naida.com",
                "published": True,
                "city_id": 20,
                "type_id": 1,
                "opening": "01:01:02",
                "closing": "06:00:07",
                "geo_location": "-56.96075, 4.25388"
            },
            {
                "name": "sit amet,",
                "address": "7048 Est. Av.",
                "phone": "0110043307",
                "email": "blandit@nullaatsem.net",
                "web_site": "www.Brenna.com",
                "published": False,
                "city_id": 9,
                "type_id": 1,
                "opening": "06:09:07",
                "closing": "04:00:05",
                "geo_location": "-15.46502, -45.26546"
            },
            {
                "name": "Sed malesuada",
                "address": "P.O. Box 908, 8634 Ante Street",
                "phone": "0685110509",
                "email": "vulputate.nisi.sem@velarcu.co.uk",
                "web_site": "www.Kerry.com",
                "published": False,
                "city_id": 11,
                "type_id": 1,
                "opening": "01:00:09",
                "closing": "01:09:06",
                "geo_location": "-3.35789, -144.61341"
            },
            {
                "name": "nibh. Phasellus",
                "address": "5291 Nibh Road",
                "phone": "0334717141",
                "email": "dictum.cursus@nunc.net",
                "web_site": "www.Vera.com",
                "published": True,
                "city_id": 15,
                "type_id": 2,
                "opening": "09:06:05",
                "closing": "03:03:09",
                "geo_location": "-18.63148, 62.93381"
            },
            {
                "name": "sed dictum",
                "address": "Ap #280-4406 Nunc. Road",
                "phone": "0269099396",
                "email": "pede.nec.ante@rutrumFuscedolor.ca",
                "web_site": "www.Tashya.com",
                "published": True,
                "city_id": 18,
                "type_id": 1,
                "opening": "08:01:03",
                "closing": "09:08:02",
                "geo_location": "24.14767, 139.14041"
            },
            {
                "name": "tincidunt tempus",
                "address": "Ap #393-661 Lacus. Rd.",
                "phone": "0345425357",
                "email": "sed@estMauris.ca",
                "web_site": "www.Tashya.com",
                "published": True,
                "city_id": 9,
                "type_id": 2,
                "opening": "00:07:04",
                "closing": "03:05:05",
                "geo_location": "-54.38585, 73.85012"
            },
            {
                "name": "felis. Donec",
                "address": "6859 Non Road",
                "phone": "0629619013",
                "email": "id.ante.Nunc@velitdui.ca",
                "web_site": "www.Hadley.com",
                "published": True,
                "city_id": 16,
                "type_id": 1,
                "opening": "03:01:07",
                "closing": "02:06:00",
                "geo_location": "64.08712, -97.61999"
            },
            {
                "name": "interdum libero",
                "address": "703-4828 Congue Rd.",
                "phone": "0643954496",
                "email": "et@acarcu.edu",
                "web_site": "www.Mia.com",
                "published": True,
                "city_id": 2,
                "type_id": 1,
                "opening": "02:01:05",
                "closing": "02:05:04",
                "geo_location": "-51.92191, -90.45693"
            },
            {
                "name": "sit amet",
                "address": "Ap #901-558 Sed, Ave",
                "phone": "0959468226",
                "email": "vel.sapien@suscipitnonummy.edu",
                "web_site": "www.Eliana.com",
                "published": True,
                "city_id": 13,
                "type_id": 1,
                "opening": "00:04:03",
                "closing": "09:02:02",
                "geo_location": "55.60175, -56.94225"
            },
            {
                "name": "dictum augue",
                "address": "P.O. Box 223, 333 Neque Rd.",
                "phone": "0726724867",
                "email": "enim@dolorsit.edu",
                "web_site": "www.Quon.com",
                "published": True,
                "city_id": 18,
                "type_id": 1,
                "opening": "01:06:06",
                "closing": "00:05:05",
                "geo_location": "-76.41768, -152.44933"
            },
            {
                "name": "mauris. Suspendisse",
                "address": "314-8854 Netus St.",
                "phone": "0190206677",
                "email": "blandit@etmagnis.ca",
                "web_site": "www.Illiana.com",
                "published": False,
                "city_id": 1,
                "type_id": 1,
                "opening": "09:01:09",
                "closing": "07:06:03",
                "geo_location": "-73.95534, -21.74837"
            },
            {
                "name": "ac metus",
                "address": "7155 Curabitur St.",
                "phone": "0924243680",
                "email": "mauris.sit@tinciduntvehicularisus.com",
                "web_site": "www.Irene.com",
                "published": False,
                "city_id": 16,
                "type_id": 1,
                "opening": "00:07:05",
                "closing": "00:08:01",
                "geo_location": "17.98333, 15.95371"
            },
            {
                "name": "ullamcorper, nisl",
                "address": "Ap #709-7778 Viverra. St.",
                "phone": "0795067586",
                "email": "est.Nunc.laoreet@Mauriseu.co.uk",
                "web_site": "www.Eliana.com",
                "published": False,
                "city_id": 12,
                "type_id": 1,
                "opening": "03:07:08",
                "closing": "07:09:06",
                "geo_location": "79.47434, 33.70176"
            },
            {
                "name": "semper pretium",
                "address": "Ap #557-3524 In, St.",
                "phone": "0474427052",
                "email": "eros@inmagnaPhasellus.ca",
                "web_site": "www.Deanna.com",
                "published": False,
                "city_id": 2,
                "type_id": 1,
                "opening": "04:03:02",
                "closing": "02:05:01",
                "geo_location": "-7.82319, 154.42741"
            },
            {
                "name": "Donec porttitor",
                "address": "9688 Praesent Rd.",
                "phone": "0520003189",
                "email": "velit@ut.org",
                "web_site": "www.Kevyn.com",
                "published": False,
                "city_id": 12,
                "type_id": 1,
                "opening": "06:06:04",
                "closing": "00:00:07",
                "geo_location": "-19.49241, -85.81735"
            },
            {
                "name": "magnis dis",
                "address": "8019 Dolor Avenue",
                "phone": "0585266191",
                "email": "pellentesque@malesuadaut.ca",
                "web_site": "www.Alana.com",
                "published": True,
                "city_id": 6,
                "type_id": 1,
                "opening": "00:02:07",
                "closing": "05:04:07",
                "geo_location": "-35.39925, 108.26508"
            },
            {
                "name": "justo faucibus",
                "address": "Ap #323-1781 Donec Street",
                "phone": "0293863825",
                "email": "vel.arcu.eu@orcilacus.edu",
                "web_site": "www.Freya.com",
                "published": True,
                "city_id": 2,
                "type_id": 2,
                "opening": "01:05:05",
                "closing": "04:01:00",
                "geo_location": "-23.10678, -31.34729"
            },
            {
                "name": "at lacus.",
                "address": "5594 Diam St.",
                "phone": "0345902406",
                "email": "fringilla.Donec.feugiat@arcuiaculisenim.net",
                "web_site": "www.Ifeoma.com",
                "published": True,
                "city_id": 15,
                "type_id": 1,
                "opening": "05:02:02",
                "closing": "08:00:02",
                "geo_location": "45.83085, -82.72382"
            },
            {
                "name": "diam lorem,",
                "address": "Ap #757-9943 A Road",
                "phone": "0711407732",
                "email": "euismod.mauris.eu@dictum.ca",
                "web_site": "www.MacKensie.com",
                "published": True,
                "city_id": 11,
                "type_id": 2,
                "opening": "02:00:00",
                "closing": "03:08:06",
                "geo_location": "-42.0422, 155.04126"
            },
            {
                "name": "venenatis a,",
                "address": "Ap #353-1695 Molestie St.",
                "phone": "0668709422",
                "email": "lobortis.Class.aptent@litoratorquentper.ca",
                "web_site": "www.Patricia.com",
                "published": True,
                "city_id": 14,
                "type_id": 1,
                "opening": "07:03:02",
                "closing": "07:06:01",
                "geo_location": "-59.46743, -11.21562"
            },
            {
                "name": "ipsum. Curabitur",
                "address": "P.O. Box 839, 6046 Dolor Ave",
                "phone": "0981593909",
                "email": "urna@mattissemper.net",
                "web_site": "www.Adrienne.com",
                "published": True,
                "city_id": 7,
                "type_id": 2,
                "opening": "09:02:02",
                "closing": "04:06:09",
                "geo_location": "4.30909, 3.9021"
            },
            {
                "name": "nascetur ridiculus",
                "address": "838-568 Purus. Avenue",
                "phone": "0809499240",
                "email": "magnis.dis@ultriciesdignissim.edu",
                "web_site": "www.Farrah.com",
                "published": True,
                "city_id": 8,
                "type_id": 1,
                "opening": "07:05:03",
                "closing": "08:03:02",
                "geo_location": "59.23908, 140.74685"
            },
            {
                "name": "Pellentesque habitant",
                "address": "8399 Eleifend St.",
                "phone": "0331833288",
                "email": "ornare.sagittis.felis@elitfermentumrisus.com",
                "web_site": "www.Victoria.com",
                "published": True,
                "city_id": 12,
                "type_id": 1,
                "opening": "05:01:06",
                "closing": "06:08:07",
                "geo_location": "-79.88558, -107.9036"
            },
            {
                "name": "Quisque libero",
                "address": "535-2248 Euismod St.",
                "phone": "0535789458",
                "email": "dis.parturient.montes@massa.edu",
                "web_site": "www.Cassady.com",
                "published": False,
                "city_id": 10,
                "type_id": 2,
                "opening": "07:05:00",
                "closing": "03:02:01",
                "geo_location": "-71.96665, 159.36689"
            },
            {
                "name": "Pellentesque habitant",
                "address": "Ap #512-4888 Vehicula Ave",
                "phone": "0777398018",
                "email": "euismod.ac.fermentum@lacus.edu",
                "web_site": "www.Kevyn.com",
                "published": False,
                "city_id": 5,
                "type_id": 2,
                "opening": "01:08:00",
                "closing": "01:03:03",
                "geo_location": "-83.61071, -137.21971"
            },
            {
                "name": "sagittis semper.",
                "address": "4714 Massa. Avenue",
                "phone": "0917563331",
                "email": "magna.et@aultricies.net",
                "web_site": "www.Maile.com",
                "published": False,
                "city_id": 6,
                "type_id": 1,
                "opening": "03:04:04",
                "closing": "01:08:04",
                "geo_location": "-68.88092, 80.88263"
            },
            {
                "name": "ante ipsum",
                "address": "888-8736 Arcu. Ave",
                "phone": "0390951351",
                "email": "dolor.Donec.fringilla@Donec.com",
                "web_site": "www.Meghan.com",
                "published": True,
                "city_id": 16,
                "type_id": 1,
                "opening": "04:09:01",
                "closing": "00:06:04",
                "geo_location": "62.03075, 169.27154"
            },
            {
                "name": "auctor, velit",
                "address": "763-7856 Cum Road",
                "phone": "0693250258",
                "email": "et.lacinia@egestaslaciniaSed.ca",
                "web_site": "www.Madaline.com",
                "published": True,
                "city_id": 15,
                "type_id": 2,
                "opening": "05:08:09",
                "closing": "01:08:08",
                "geo_location": "-36.47104, 27.89919"
            },
            {
                "name": "Mauris ut",
                "address": "P.O. Box 554, 1856 Eu, St.",
                "phone": "0523027599",
                "email": "nec.ligula@Aeneansedpede.ca",
                "web_site": "www.Anastasia.com",
                "published": False,
                "city_id": 7,
                "type_id": 2,
                "opening": "09:06:05",
                "closing": "02:09:09",
                "geo_location": "2.55961, 17.07935"
            },
            {
                "name": "nunc sit",
                "address": "7209 Justo. Street",
                "phone": "0676030768",
                "email": "ac@Duis.edu",
                "web_site": "www.Lillith.com",
                "published": False,
                "city_id": 18,
                "type_id": 2,
                "opening": "09:01:00",
                "closing": "01:04:00",
                "geo_location": "62.77923, 99.29"
            },
            {
                "name": "faucibus leo,",
                "address": "3341 Orci Rd.",
                "phone": "0340993480",
                "email": "dictum@DonecnibhQuisque.org",
                "web_site": "www.Lacy.com",
                "published": False,
                "city_id": 12,
                "type_id": 1,
                "opening": "09:03:03",
                "closing": "02:06:05",
                "geo_location": "-27.00738, -71.46569"
            },
            {
                "name": "nibh. Donec",
                "address": "Ap #226-9073 Enim Rd.",
                "phone": "0846993134",
                "email": "Phasellus.libero@magna.org",
                "web_site": "www.Blythe.com",
                "published": True,
                "city_id": 16,
                "type_id": 1,
                "opening": "09:03:08",
                "closing": "03:08:05",
                "geo_location": "-10.21309, -4.33285"
            },
            {
                "name": "ac sem",
                "address": "750-1339 Dui St.",
                "phone": "0735456037",
                "email": "Etiam@nisi.com",
                "web_site": "www.Echo.com",
                "published": True,
                "city_id": 5,
                "type_id": 1,
                "opening": "03:09:09",
                "closing": "00:02:04",
                "geo_location": "88.55195, -37.55415"
            },
            {
                "name": "hymenaeos. Mauris",
                "address": "Ap #786-6568 Nisi Street",
                "phone": "0325852113",
                "email": "convallis.est@interdumenimnon.ca",
                "web_site": "www.Heather.com",
                "published": True,
                "city_id": 20,
                "type_id": 2,
                "opening": "01:09:00",
                "closing": "00:05:04",
                "geo_location": "83.1926, 128.0006"
            },
            {
                "name": "et ipsum",
                "address": "9153 At St.",
                "phone": "0823196878",
                "email": "Sed@orci.ca",
                "web_site": "www.Shelby.com",
                "published": True,
                "city_id": 6,
                "type_id": 1,
                "opening": "06:02:08",
                "closing": "05:03:03",
                "geo_location": "-60.68715, 58.7629"
            },
            {
                "name": "quis, pede.",
                "address": "Ap #965-6860 Mi. Av.",
                "phone": "0884113337",
                "email": "quis.massa@cursusIntegermollis.co.uk",
                "web_site": "www.Madeline.com",
                "published": False,
                "city_id": 7,
                "type_id": 2,
                "opening": "09:02:00",
                "closing": "00:04:09",
                "geo_location": "61.4993, -117.92615"
            },
            {
                "name": "vel, convallis",
                "address": "P.O. Box 263, 8510 Ut, Rd.",
                "phone": "0400261258",
                "email": "ornare@posuere.com",
                "web_site": "www.Angelica.com",
                "published": False,
                "city_id": 12,
                "type_id": 2,
                "opening": "01:09:03",
                "closing": "05:04:03",
                "geo_location": "-17.76305, 175.10457"
            },
            {
                "name": "non dui",
                "address": "252-5204 Eu Street",
                "phone": "0349095426",
                "email": "nisi@pedeetrisus.ca",
                "web_site": "www.Chanda.com",
                "published": False,
                "city_id": 11,
                "type_id": 2,
                "opening": "04:08:06",
                "closing": "02:09:02",
                "geo_location": "-36.6437, 53.6932"
            },
            {
                "name": "mi tempor",
                "address": "536-8524 Mollis Street",
                "phone": "0172440876",
                "email": "Cum.sociis@ridiculusmusProin.com",
                "web_site": "www.Vanna.com",
                "published": True,
                "city_id": 9,
                "type_id": 1,
                "opening": "03:08:01",
                "closing": "00:00:09",
                "geo_location": "73.49272, -11.52942"
            },
            {
                "name": "nec tellus.",
                "address": "P.O. Box 397, 3836 Magnis St.",
                "phone": "0403427100",
                "email": "inceptos.hymenaeos@elementumloremut.edu",
                "web_site": "www.September.com",
                "published": True,
                "city_id": 12,
                "type_id": 1,
                "opening": "02:01:06",
                "closing": "00:03:04",
                "geo_location": "18.78666, 145.3204"
            },
            {
                "name": "nisi nibh",
                "address": "325-3447 Interdum. Rd.",
                "phone": "0834175955",
                "email": "euismod.ac.fermentum@In.org",
                "web_site": "www.Heather.com",
                "published": False,
                "city_id": 3,
                "type_id": 2,
                "opening": "02:02:07",
                "closing": "07:05:00",
                "geo_location": "-40.30339, 126.06477"
            },
            {
                "name": "Mauris vel",
                "address": "7818 Nunc Av.",
                "phone": "0303130291",
                "email": "mi@ipsumSuspendisse.net",
                "web_site": "www.MacKenzie.com",
                "published": True,
                "city_id": 12,
                "type_id": 2,
                "opening": "08:07:06",
                "closing": "07:04:02",
                "geo_location": "-11.34737, 102.76519"
            },
            {
                "name": "Proin ultrices.",
                "address": "188-5541 Pretium Av.",
                "phone": "0437275602",
                "email": "blandit.at.nisi@Nuncsedorci.net",
                "web_site": "www.Zenia.com",
                "published": True,
                "city_id": 10,
                "type_id": 2,
                "opening": "09:01:08",
                "closing": "00:00:03",
                "geo_location": "87.23851, 43.44818"
            },
            {
                "name": "egestas hendrerit",
                "address": "Ap #719-3037 Dolor. Avenue",
                "phone": "0429118368",
                "email": "adipiscing@tellus.com",
                "web_site": "www.Jessamine.com",
                "published": True,
                "city_id": 2,
                "type_id": 2,
                "opening": "00:07:07",
                "closing": "02:06:07",
                "geo_location": "77.15911, -5.10948"
            },
            {
                "name": "dolor, tempus",
                "address": "Ap #834-9305 Scelerisque St.",
                "phone": "0467292728",
                "email": "gravida@imperdietnec.ca",
                "web_site": "www.MacKenzie.com",
                "published": True,
                "city_id": 8,
                "type_id": 1,
                "opening": "02:00:00",
                "closing": "04:03:06",
                "geo_location": "52.38303, -131.72267"
            },
            {
                "name": "eleifend vitae,",
                "address": "P.O. Box 831, 5505 Aliquam Rd.",
                "phone": "0906751447",
                "email": "risus@Curabitursed.edu",
                "web_site": "www.Lillith.com",
                "published": True,
                "city_id": 11,
                "type_id": 2,
                "opening": "07:01:07",
                "closing": "02:04:04",
                "geo_location": "-33.68815, -53.82664"
            },
            {
                "name": "laoreet, libero",
                "address": "7454 Vitae, Street",
                "phone": "0591322926",
                "email": "purus.sapien.gravida@Quisquenonummy.ca",
                "web_site": "www.Shana.com",
                "published": True,
                "city_id": 3,
                "type_id": 2,
                "opening": "01:05:09",
                "closing": "04:07:05",
                "geo_location": "65.15583, -66.15915"
            },
            {
                "name": "Nam consequat",
                "address": "2220 Class Road",
                "phone": "0452046080",
                "email": "dis.parturient@nuncsitamet.ca",
                "web_site": "www.Rachel.com",
                "published": False,
                "city_id": 14,
                "type_id": 1,
                "opening": "02:07:00",
                "closing": "04:00:04",
                "geo_location": "-81.11875, -112.68215"
            },
            {
                "name": "libero nec",
                "address": "3046 Semper St.",
                "phone": "0945922039",
                "email": "Donec.consectetuer@est.edu",
                "web_site": "www.Macy.com",
                "published": True,
                "city_id": 7,
                "type_id": 2,
                "opening": "06:06:08",
                "closing": "02:00:03",
                "geo_location": "37.98891, -150.6637"
            },
            {
                "name": "felis. Donec",
                "address": "Ap #698-733 Arcu Rd.",
                "phone": "0798651815",
                "email": "egestas@nullaIntincidunt.co.uk",
                "web_site": "www.Shay.com",
                "published": False,
                "city_id": 13,
                "type_id": 1,
                "opening": "03:05:01",
                "closing": "09:03:07",
                "geo_location": "-32.86052, -72.77358"
            },
            {
                "name": "In faucibus.",
                "address": "Ap #494-2513 Curabitur St.",
                "phone": "0658593045",
                "email": "neque.et.nunc@tellusid.ca",
                "web_site": "www.Jacqueline.com",
                "published": False,
                "city_id": 14,
                "type_id": 1,
                "opening": "00:04:06",
                "closing": "07:07:04",
                "geo_location": "51.18301, -145.2063"
            },
            {
                "name": "Nulla interdum.",
                "address": "116 Dolor. St.",
                "phone": "0649163349",
                "email": "blandit.at@lectus.com",
                "web_site": "www.Danielle.com",
                "published": True,
                "city_id": 7,
                "type_id": 2,
                "opening": "08:04:06",
                "closing": "01:06:01",
                "geo_location": "-46.14085, 145.99098"
            },
            {
                "name": "nec orci.",
                "address": "P.O. Box 247, 8375 Quisque Street",
                "phone": "0672580133",
                "email": "urna.et@enimnislelementum.ca",
                "web_site": "www.Iona.com",
                "published": False,
                "city_id": 6,
                "type_id": 2,
                "opening": "07:02:05",
                "closing": "08:06:00",
                "geo_location": "-50.65701, -77.29522"
            },
            {
                "name": "elit, a",
                "address": "5446 Convallis Ave",
                "phone": "0320280406",
                "email": "nunc.interdum@nullaIntegerurna.co.uk",
                "web_site": "www.Kerry.com",
                "published": False,
                "city_id": 6,
                "type_id": 1,
                "opening": "06:08:05",
                "closing": "06:06:02",
                "geo_location": "-54.80976, 98.20262"
            },
            {
                "name": "magna. Praesent",
                "address": "1990 Sed Ave",
                "phone": "0437386217",
                "email": "ante.ipsum@Curabitursed.ca",
                "web_site": "www.Willa.com",
                "published": False,
                "city_id": 18,
                "type_id": 2,
                "opening": "09:09:09",
                "closing": "06:06:09",
                "geo_location": "-42.88374, 123.75516"
            },
            {
                "name": "at, nisi.",
                "address": "5390 Eu, Ave",
                "phone": "0908043586",
                "email": "dictum@tacitisociosquad.co.uk",
                "web_site": "www.Inga.com",
                "published": False,
                "city_id": 10,
                "type_id": 1,
                "opening": "02:07:01",
                "closing": "09:06:08",
                "geo_location": "-22.32683, -159.25654"
            },
            {
                "name": "arcu. Aliquam",
                "address": "669-2128 In Av.",
                "phone": "0336467758",
                "email": "ornare.In@arcu.com",
                "web_site": "www.Amelia.com",
                "published": True,
                "city_id": 5,
                "type_id": 1,
                "opening": "02:00:08",
                "closing": "01:02:07",
                "geo_location": "87.00617, -133.00005"
            },
            {
                "name": "tempor augue",
                "address": "1944 Dictum. St.",
                "phone": "0821501758",
                "email": "quis@auctornuncnulla.ca",
                "web_site": "www.Claire.com",
                "published": True,
                "city_id": 13,
                "type_id": 2,
                "opening": "01:05:01",
                "closing": "05:07:02",
                "geo_location": "87.85242, -6.29938"
            },
            {
                "name": "Duis at",
                "address": "P.O. Box 882, 4323 Nulla Rd.",
                "phone": "0363138464",
                "email": "lobortis@etarcuimperdiet.net",
                "web_site": "www.Ruby.com",
                "published": False,
                "city_id": 6,
                "type_id": 1,
                "opening": "07:07:07",
                "closing": "04:04:06",
                "geo_location": "73.5267, 65.59743"
            },
            {
                "name": "placerat, orci",
                "address": "P.O. Box 223, 3236 Aliquam Road",
                "phone": "0470811936",
                "email": "justo.eu@arcu.co.uk",
                "web_site": "www.Megan.com",
                "published": True,
                "city_id": 11,
                "type_id": 1,
                "opening": "06:07:04",
                "closing": "07:05:00",
                "geo_location": "69.37725, -149.58209"
            },
            {
                "name": "id sapien.",
                "address": "937-7984 Et Road",
                "phone": "0739335827",
                "email": "sem.vitae.aliquam@Fuscealiquam.com",
                "web_site": "www.Casey.com",
                "published": False,
                "city_id": 19,
                "type_id": 1,
                "opening": "08:04:08",
                "closing": "04:08:04",
                "geo_location": "-77.99732, 34.40799"
            },
            {
                "name": "vitae nibh.",
                "address": "Ap #765-3405 Scelerisque Rd.",
                "phone": "0277020058",
                "email": "nascetur.ridiculus@Sed.ca",
                "web_site": "www.Amber.com",
                "published": True,
                "city_id": 4,
                "type_id": 2,
                "opening": "01:03:06",
                "closing": "00:08:05",
                "geo_location": "-15.48762, -127.76981"
            },
            {
                "name": "commodo hendrerit.",
                "address": "P.O. Box 885, 6459 Cras Street",
                "phone": "0902697357",
                "email": "lobortis@metusurnaconvallis.ca",
                "web_site": "www.Hedda.com",
                "published": False,
                "city_id": 17,
                "type_id": 2,
                "opening": "02:01:04",
                "closing": "05:09:05",
                "geo_location": "-29.98681, 13.0319"
            },
            {
                "name": "Pellentesque tincidunt",
                "address": "Ap #220-5287 Rutrum St.",
                "phone": "0715637725",
                "email": "nisl@Classaptent.com",
                "web_site": "www.Basia.com",
                "published": True,
                "city_id": 16,
                "type_id": 1,
                "opening": "09:00:00",
                "closing": "02:01:01",
                "geo_location": "-55.78835, -30.25566"
            },
            {
                "name": "Phasellus at",
                "address": "348-5475 Purus Rd.",
                "phone": "0572567603",
                "email": "Curabitur.dictum@Aenean.edu",
                "web_site": "www.Joelle.com",
                "published": False,
                "city_id": 15,
                "type_id": 2,
                "opening": "06:05:07",
                "closing": "01:02:02",
                "geo_location": "80.61854, 39.91801"
            },
            {
                "name": "Pellentesque habitant",
                "address": "Ap #671-7099 Mi St.",
                "phone": "0687787465",
                "email": "vitae.dolor.Donec@idrisusquis.net",
                "web_site": "www.Bethany.com",
                "published": True,
                "city_id": 7,
                "type_id": 1,
                "opening": "06:01:02",
                "closing": "05:03:02",
                "geo_location": "31.50775, 179.76498"
            },
            {
                "name": "Lorem ipsum",
                "address": "7881 Suspendisse Street",
                "phone": "0976334829",
                "email": "Proin.dolor.Nulla@cursus.net",
                "web_site": "www.Dorothy.com",
                "published": True,
                "city_id": 3,
                "type_id": 2,
                "opening": "00:02:09",
                "closing": "05:01:07",
                "geo_location": "-46.48765, -54.11185"
            },
            {
                "name": "vel sapien",
                "address": "Ap #951-6481 Tellus, Avenue",
                "phone": "0691791880",
                "email": "est.vitae@adipiscingelitEtiam.com",
                "web_site": "www.Jena.com",
                "published": False,
                "city_id": 10,
                "type_id": 1,
                "opening": "03:08:01",
                "closing": "05:09:03",
                "geo_location": "62.93435, 58.76696"
            },
            {
                "name": "massa rutrum",
                "address": "P.O. Box 491, 6138 Phasellus Av.",
                "phone": "0990818104",
                "email": "felis.Nulla.tempor@feugiatmetus.co.uk",
                "web_site": "www.Illana.com",
                "published": False,
                "city_id": 14,
                "type_id": 1,
                "opening": "06:05:00",
                "closing": "02:07:06",
                "geo_location": "-74.11176, 8.8753"
            },
            {
                "name": "vitae sodales",
                "address": "742-3126 Eu Street",
                "phone": "0390905437",
                "email": "dis.parturient@malesuada.net",
                "web_site": "www.Skyler.com",
                "published": False,
                "city_id": 15,
                "type_id": 2,
                "opening": "07:09:08",
                "closing": "08:08:04",
                "geo_location": "26.50641, 176.66682"
            },
            {
                "name": "eu dui.",
                "address": "4673 Nam Rd.",
                "phone": "0885065101",
                "email": "cursus.a@velit.org",
                "web_site": "www.Mari.com",
                "published": False,
                "city_id": 17,
                "type_id": 1,
                "opening": "04:04:05",
                "closing": "08:01:09",
                "geo_location": "-51.97088, -36.53867"
            },
            {
                "name": "Phasellus dolor",
                "address": "Ap #253-4508 Eget St.",
                "phone": "0614076838",
                "email": "est@arcuVestibulumante.com",
                "web_site": "www.Hedy.com",
                "published": False,
                "city_id": 5,
                "type_id": 1,
                "opening": "09:08:08",
                "closing": "09:06:09",
                "geo_location": "-51.52846, 34.27042"
            },
            {
                "name": "in felis.",
                "address": "120-8826 Ipsum Av.",
                "phone": "0640286530",
                "email": "odio.auctor.vitae@utsem.org",
                "web_site": "www.Demetria.com",
                "published": True,
                "city_id": 18,
                "type_id": 2,
                "opening": "07:08:04",
                "closing": "03:03:02",
                "geo_location": "71.64229, -60.45883"
            },
            {
                "name": "adipiscing non,",
                "address": "P.O. Box 897, 1995 Sit Street",
                "phone": "0512549145",
                "email": "ornare.In@Integervitaenibh.com",
                "web_site": "www.Wendy.com",
                "published": True,
                "city_id": 19,
                "type_id": 1,
                "opening": "07:00:00",
                "closing": "01:01:01",
                "geo_location": "-1.42435, 26.96433"
            }
        ]
                   )


def downgrade():
    op.drop_table('centers')
    op.drop_table('centerType')
    op.drop_table('city')

