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
from sqlalchemy.dialects.mysql import ENUM

revision = 'ca9f929dd635'
down_revision = '6b6bd5f86431'
branch_labels = None
depends_on = None

STATES = ('pending', 'approved', 'rejected')
STATE_ENUM = ENUM(*STATES, name='state')
CENTER_TYPES = ('alimentos', 'general', 'salud')
CENTER_TYPES_ENUM = ENUM(*CENTER_TYPES, name='type')


def upgrade():
    city_table = op.create_table(
        'city',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(100), nullable=False),
    )
    centers_table = op.create_table(
        'centers',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('email', sa.String(60), nullable=False),
        sa.Column('name', sa.String(40), nullable=False),
        sa.Column('address', sa.String(100), nullable=True),
        sa.Column('phone', sa.String(20)),
        sa.Column('web_site', sa.String(40)),
        sa.Column('published', sa.Boolean(), default=False),
        sa.Column('gl_lat', sa.String(30)),
        sa.Column('gl_long', sa.String(30)),
        sa.Column('opening', sa.Time()),
        sa.Column('closing', sa.Time()),
        sa.Column('state', STATE_ENUM),
        sa.Column('protocol', sa.dialects.mysql.LONGBLOB()),
        sa.Column('city_id', sa.Integer, ForeignKey('city.id')),
        sa.Column('type', CENTER_TYPES_ENUM),
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
                           "name": "Toledo"
                       },
                       {
                           "name": "Alva"
                       },
                       {
                           "name": "Independence"
                       }
                   ])

    centers = [
        {
            "name": "Deacon Mcgowan",
            "address": "569 Proin Ave",
            "phone": "(113) 744-3458",
            "email": "luctus.et.ultrices@vestibulumlorem.com",
            "web_site": "https://www.Felicia.com",
            "city_id": 8,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "-39.42783, -131.22992"
        },
        {
            "name": "Yuli Powell",
            "address": "P.O. Box 609, 8564 Metus. Road",
            "phone": "(934) 281-6656",
            "email": "vel@tellus.edu",
            "web_site": "https://www.Tatiana.com",
            "city_id": 17,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "-73.07459, 110.51013"
        },
        {
            "name": "Linus Camacho",
            "address": "P.O. Box 698, 9129 Fringilla. St.",
            "phone": "(872) 148-4734",
            "email": "ut@euligulaAenean.com",
            "web_site": "https://www.Jane.com",
            "city_id": 22,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "43.8134, -68.89941"
        },
        {
            "name": "Joshua Blankenship",
            "address": "428-1289 Urna. Av.",
            "phone": "(473) 165-2064",
            "email": "Suspendisse.sagittis.Nullam@Proin.org",
            "web_site": "https://www.Angelica.com",
            "city_id": 23,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "-20.41078, -23.12832"
        },
        {
            "name": "Chaim Watson",
            "address": "P.O. Box 858, 5148 Duis Av.",
            "phone": "(961) 321-3809",
            "email": "ullamcorper.Duis.at@non.co.uk",
            "web_site": "https://www.Renee.com",
            "city_id": 30,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "60.17464, -108.22611"
        },
        {
            "name": "Fulton Simon",
            "address": "966 Feugiat Avenue",
            "phone": "(995) 878-8690",
            "email": "Donec@ullamcorper.edu",
            "web_site": "https://www.Ciara.com",
            "city_id": 7,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "-72.98666, -121.59964"
        },
        {
            "name": "Bert Marquez",
            "address": "Ap #445-6941 Curabitur Street",
            "phone": "(935) 722-0605",
            "email": "vulputate.mauris@sagittis.co.uk",
            "web_site": "https://www.Lunea.com",
            "city_id": 3,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "8.67668, -155.07677"
        },
        {
            "name": "Paul Howell",
            "address": "Ap #703-6249 Lorem Street",
            "phone": "(428) 942-5676",
            "email": "Donec.consectetuer.mauris@fermentumconvallisligula.com",
            "web_site": "https://www.Xena.com",
            "city_id": 3,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "54.42302, 10.20175"
        },
        {
            "name": "Berk Phillips",
            "address": "P.O. Box 992, 3922 Felis Rd.",
            "phone": "(378) 112-4191",
            "email": "neque.pellentesque.massa@nullavulputatedui.ca",
            "web_site": "https://www.Beatrice.com",
            "city_id": 29,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "-30.4538, -31.3343"
        },
        {
            "name": "Avram Shields",
            "address": "746-9331 Sed Rd.",
            "phone": "(529) 655-6721",
            "email": "montes@dolornonummyac.org",
            "web_site": "https://www.Pascale.com",
            "city_id": 20,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "-70.42086, 123.8907"
        },
        {
            "name": "Clayton Myers",
            "address": "1311 Feugiat St.",
            "phone": "(417) 129-2054",
            "email": "tincidunt.aliquam.arcu@urna.com",
            "web_site": "https://www.Christen.com",
            "city_id": 30,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "40.52007, 11.28166"
        },
        {
            "name": "Chadwick Rhodes",
            "address": "3433 Fringilla Rd.",
            "phone": "(776) 279-0090",
            "email": "Donec.dignissim@tempusrisusDonec.net",
            "web_site": "https://www.Lila.com",
            "city_id": 13,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "75.9892, 33.40298"
        },
        {
            "name": "Hector Lane",
            "address": "Ap #331-2744 Vehicula Avenue",
            "phone": "(856) 522-5302",
            "email": "neque.In.ornare@magnaSuspendissetristique.org",
            "web_site": "https://www.Kim.com",
            "city_id": 9,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "74.97436, 21.7691"
        },
        {
            "name": "Cody Kane",
            "address": "P.O. Box 897, 6712 Sit St.",
            "phone": "(869) 655-2286",
            "email": "cursus@vehicula.com",
            "web_site": "https://www.Chantale.com",
            "city_id": 12,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "29.37252, 42.6547"
        },
        {
            "name": "Logan Garner",
            "address": "124-807 Nunc Avenue",
            "phone": "(432) 796-2476",
            "email": "vehicula@adipiscing.org",
            "web_site": "https://www.Xaviera.com",
            "city_id": 4,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "-82.72105, -36.19353"
        },
        {
            "name": "Nero Kaufman",
            "address": "2745 Sem Rd.",
            "phone": "(162) 393-0548",
            "email": "Aliquam.ornare@Nuncmaurissapien.co.uk",
            "web_site": "https://www.Morgan.com",
            "city_id": 20,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "-64.88058, 43.42009"
        },
        {
            "name": "Hamilton Knowles",
            "address": "9765 Tristique Road",
            "phone": "(787) 442-9462",
            "email": "id.ante@temporaugueac.com",
            "web_site": "https://www.Evangeline.com",
            "city_id": 17,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "-58.23742, -53.6479"
        },
        {
            "name": "Chancellor Sutton",
            "address": "Ap #241-6900 Arcu. Avenue",
            "phone": "(424) 143-4881",
            "email": "elementum.lorem@risus.com",
            "web_site": "https://www.Sybill.com",
            "city_id": 25,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "-23.08501, 114.58898"
        },
        {
            "name": "Vincent Molina",
            "address": "P.O. Box 544, 538 Orci Street",
            "phone": "(357) 424-6702",
            "email": "massa@Sedmolestie.com",
            "web_site": "https://www.Neve.com",
            "city_id": 14,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "29.1554, -58.39153"
        },
        {
            "name": "Zeph Alvarado",
            "address": "876-6771 Magnis Ave",
            "phone": "(608) 804-5874",
            "email": "semper.egestas@etmagnis.org",
            "web_site": "https://www.Tatyana.com",
            "city_id": 15,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "-64.13474, 24.90177"
        },
        {
            "name": "David Lester",
            "address": "7354 Id, Rd.",
            "phone": "(755) 122-6855",
            "email": "massa.non@ategestas.ca",
            "web_site": "https://www.Mariam.com",
            "city_id": 20,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "2.09674, 91.37508"
        },
        {
            "name": "Arthur Vinson",
            "address": "P.O. Box 191, 4376 Eros St.",
            "phone": "(408) 495-8361",
            "email": "Cum.sociis@enim.edu",
            "web_site": "https://www.Zenaida.com",
            "city_id": 28,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "8.64294, -71.38021"
        },
        {
            "name": "Hyatt Medina",
            "address": "474-8811 Convallis St.",
            "phone": "(585) 666-1233",
            "email": "sed.pede@a.org",
            "web_site": "https://www.Rae.com",
            "city_id": 29,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "60.10816, -104.05721"
        },
        {
            "name": "Guy Hodge",
            "address": "1977 Arcu. Street",
            "phone": "(505) 241-1741",
            "email": "dui.semper@feugiattellus.ca",
            "web_site": "https://www.Isabelle.com",
            "city_id": 7,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "-84.43946, -15.15763"
        },
        {
            "name": "Chaim Callahan",
            "address": "Ap #921-5933 A Av.",
            "phone": "(338) 849-4080",
            "email": "nec.euismod.in@risusNuncac.co.uk",
            "web_site": "https://www.Donna.com",
            "city_id": 29,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "-80.37991, 60.47264"
        },
        {
            "name": "Griffith Flores",
            "address": "550-9925 Rhoncus. Rd.",
            "phone": "(639) 681-4542",
            "email": "ultricies.ligula@pedePraesenteu.ca",
            "web_site": "https://www.Jena.com",
            "city_id": 13,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "-5.36161, 18.86378"
        },
        {
            "name": "Dustin Glenn",
            "address": "Ap #758-8042 Turpis. St.",
            "phone": "(378) 939-3041",
            "email": "est@ornareplaceratorci.co.uk",
            "web_site": "https://www.Bell.com",
            "city_id": 10,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "-0.31799, 41.28833"
        },
        {
            "name": "Timothy Noel",
            "address": "498 Risus St.",
            "phone": "(421) 641-7202",
            "email": "mauris.Suspendisse@lectusconvallisest.org",
            "web_site": "https://www.Tamekah.com",
            "city_id": 12,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "-1.08516, 145.73139"
        },
        {
            "name": "Cairo Hurst",
            "address": "Ap #621-7043 Odio Ave",
            "phone": "(151) 919-2681",
            "email": "nunc@Duisrisusodio.org",
            "web_site": "https://www.Stephanie.com",
            "city_id": 11,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "30.8473, 40.11083"
        },
        {
            "name": "Leonard Cole",
            "address": "139-8169 Blandit Road",
            "phone": "(989) 509-5587",
            "email": "orci.lobortis.augue@loremsemperauctor.net",
            "web_site": "https://www.Elaine.com",
            "city_id": 24,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "51.5266, -135.26973"
        },
        {
            "name": "Mason Scott",
            "address": "5658 Dignissim. Avenue",
            "phone": "(821) 511-1634",
            "email": "dictum.augue@aliquam.co.uk",
            "web_site": "https://www.Laura.com",
            "city_id": 20,
            "type": "general",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "rejected",
			"published": False,

            "geo_location": "-54.06222, 142.76637"
        },
        {
            "name": "Andrew Holland",
            "address": "404-1616 Nam Road",
            "phone": "(590) 252-3443",
            "email": "non.magna.Nam@mauris.co.uk",
            "web_site": "https://www.Nita.com",
            "city_id": 18,
            "type": "general",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "rejected",
			"published": False,

            "geo_location": "62.97775, 177.08708"
        },
        {
            "name": "Norman Knight",
            "address": "6914 Ligula. Rd.",
            "phone": "(773) 522-5233",
            "email": "lobortis@pedeblanditcongue.net",
            "web_site": "https://www.Meghan.com",
            "city_id": 30,
            "type": "general",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "rejected",
			"published": False,

            "geo_location": "11.42182, 149.57773"
        },
        {
            "name": "Yardley Lara",
            "address": "P.O. Box 575, 2414 Vitae Ave",
            "phone": "(509) 441-9717",
            "email": "Nulla@luctus.edu",
            "web_site": "https://www.Urielle.com",
            "city_id": 24,
            "type": "general",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "rejected",
			"published": False,

            "geo_location": "-57.58976, 155.88253"
        },
        {
            "name": "Kieran Woodard",
            "address": "9262 Quam Av.",
            "phone": "(947) 938-4912",
            "email": "Cras.interdum@Duisrisusodio.org",
            "web_site": "https://www.Rhiannon.com",
            "city_id": 10,
            "type": "general",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "rejected",
			"published": False,

            "geo_location": "44.55883, -67.81671"
        },
        {
            "name": "Paul Manning",
            "address": "181-102 Eget Street",
            "phone": "(913) 746-6058",
            "email": "lectus.justo.eu@gravida.co.uk",
            "web_site": "https://www.Hanna.com",
            "city_id": 21,
            "type": "general",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "rejected",
			"published": False,

            "geo_location": "-85.34147, 65.68446"
        },
        {
            "name": "Dennis Ward",
            "address": "5803 Aliquam Street",
            "phone": "(918) 865-7439",
            "email": "eleifend.vitae.erat@ac.co.uk",
            "web_site": "https://www.Hollee.com",
            "city_id": 9,
            "type": "general",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "rejected",
			"published": False,

            "geo_location": "78.30875, 106.18924"
        },
        {
            "name": "Buckminster Murray",
            "address": "436-1768 Ac Street",
            "phone": "(554) 298-9620",
            "email": "libero.Proin@luctus.org",
            "web_site": "https://www.Ina.com",
            "city_id": 19,
            "type": "general",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "rejected",
			"published": False,

            "geo_location": "-29.63107, 49.64374"
        },
        {
            "name": "Jesse Padilla",
            "address": "P.O. Box 512, 4709 Erat. Avenue",
            "phone": "(969) 884-4937",
            "email": "eget.ipsum.Donec@leoCrasvehicula.org",
            "web_site": "https://www.Christine.com",
            "city_id": 15,
            "type": "general",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "rejected",
			"published": False,

            "geo_location": "-70.06008, 25.50508"
        },
        {
            "name": "Bert Casey",
            "address": "P.O. Box 152, 839 In Av.",
            "phone": "(521) 773-9094",
            "email": "faucibus@atvelitCras.org",
            "web_site": "https://www.Charity.com",
            "city_id": 11,
            "type": "general",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "rejected",
			"published": False,

            "geo_location": "-29.03175, 153.50266"
        },
        {
            "name": "Brent Goodwin",
            "address": "720-5732 Primis Avenue",
            "phone": "(793) 767-4614",
            "email": "eleifend.nunc.risus@augueid.co.uk",
            "web_site": "https://www.Linda.com",
            "city_id": 3,
            "type": "general",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "rejected",
			"published": False,

            "geo_location": "-13.6171, 71.03475"
        },
        {
            "name": "David Schmidt",
            "address": "826 Ullamcorper. Rd.",
            "phone": "(290) 613-8506",
            "email": "justo@luctus.edu",
            "web_site": "https://www.Sigourney.com",
            "city_id": 7,
            "type": "general",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "rejected",
			"published": False,

            "geo_location": "-72.38899, -115.07888"
        },
        {
            "name": "Garrett Adams",
            "address": "Ap #682-7463 Phasellus Av.",
            "phone": "(534) 686-2574",
            "email": "lacus.vestibulum@risusQuisquelibero.net",
            "web_site": "https://www.Briar.com",
            "city_id": 16,
            "type": "general",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "rejected",
			"published": False,

            "geo_location": "5.80521, 10.87034"
        },
        {
            "name": "Patrick Grant",
            "address": "P.O. Box 912, 3324 Mauris St.",
            "phone": "(730) 411-4932",
            "email": "nonummy.Fusce@arcu.co.uk",
            "web_site": "https://www.Cameron.com",
            "city_id": 8,
            "type": "general",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "rejected",
			"published": False,

            "geo_location": "56.14653, 133.66836"
        },
        {
            "name": "Trevor Walsh",
            "address": "Ap #523-2052 Libero. St.",
            "phone": "(631) 552-7587",
            "email": "enim@euismodet.net",
            "web_site": "https://www.Christen.com",
            "city_id": 28,
            "type": "general",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "rejected",
			"published": False,

            "geo_location": "8.88968, -129.41991"
        },
        {
            "name": "Quentin Copeland",
            "address": "Ap #786-5633 Mauris. Road",
            "phone": "(290) 688-2067",
            "email": "pellentesque.a@necquam.net",
            "web_site": "https://www.Pandora.com",
            "city_id": 7,
            "type": "general",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "rejected",
			"published": False,

            "geo_location": "53.28283, 103.69874"
        },
        {
            "name": "Joshua Hoover",
            "address": "P.O. Box 304, 1446 Consectetuer Ave",
            "phone": "(866) 134-2495",
            "email": "tincidunt@liberolacusvarius.ca",
            "web_site": "https://www.Demetria.com",
            "city_id": 26,
            "type": "general",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "rejected",
			"published": False,

            "geo_location": "-47.01651, 80.63826"
        },
        {
            "name": "Daquan Leon",
            "address": "Ap #810-4332 Sociis Rd.",
            "phone": "(654) 188-4694",
            "email": "felis.adipiscing.fringilla@Donec.co.uk",
            "web_site": "https://www.Serina.com",
            "city_id": 16,
            "type": "general",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "rejected",
			"published": False,

            "geo_location": "-10.45212, -25.99467"
        },
        {
            "name": "Hayes Hanson",
            "address": "269-1825 A Street",
            "phone": "(225) 269-8832",
            "email": "molestie.dapibus.ligula@egestas.org",
            "web_site": "https://www.Cora.com",
            "city_id": 2,
            "type": "general",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "rejected",
			"published": False,

            "geo_location": "86.81364, -79.28977"
        },
        {
            "name": "Reece Molina",
            "address": "961-4001 Mi Rd.",
            "phone": "(908) 108-1881",
            "email": "dui.semper.et@CuraeDonectincidunt.org",
            "web_site": "https://www.Aurora.com",
            "city_id": 8,
            "type": "general",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "rejected",
			"published": False,

            "geo_location": "-25.97686, -2.64713"
        },
        {
            "name": "Eric Peck",
            "address": "P.O. Box 206, 6264 Aliquam Avenue",
            "phone": "(492) 387-3952",
            "email": "metus@vitaediam.com",
            "web_site": "https://www.Britanney.com",
            "city_id": 11,
            "type": "general",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "rejected",
			"published": False,

            "geo_location": "87.56708, -63.79444"
        },
        {
            "name": "Dane Grimes",
            "address": "P.O. Box 523, 4123 Hymenaeos. Av.",
            "phone": "(664) 901-5698",
            "email": "est.Mauris.eu@ametdiameu.edu",
            "web_site": "https://www.Lani.com",
            "city_id": 11,
            "type": "general",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "rejected",
			"published": False,

            "geo_location": "-20.54861, 120.06517"
        },
        {
            "name": "Calvin Franks",
            "address": "Ap #672-4077 Libero Road",
            "phone": "(386) 314-1537",
            "email": "Mauris@luctusipsum.net",
            "web_site": "https://www.Hedwig.com",
            "city_id": 21,
            "type": "general",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "rejected",
			"published": False,

            "geo_location": "-73.92559, -35.3757"
        },
        {
            "name": "Amir Yang",
            "address": "7571 Interdum St.",
            "phone": "(728) 585-9306",
            "email": "ipsum.dolor@necorciDonec.org",
            "web_site": "https://www.Genevieve.com",
            "city_id": 28,
            "type": "general",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "rejected",
			"published": False,

            "geo_location": "-39.34287, 35.5736"
        },
        {
            "name": "Melvin Estrada",
            "address": "Ap #689-175 Duis Ave",
            "phone": "(187) 162-5486",
            "email": "Curabitur@mollisneccursus.co.uk",
            "web_site": "https://www.Alika.com",
            "city_id": 6,
            "type": "general",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "rejected",
			"published": False,

            "geo_location": "-63.8459, -166.74882"
        },
        {
            "name": "Orson Kerr",
            "address": "P.O. Box 641, 1501 Imperdiet Ave",
            "phone": "(791) 578-1516",
            "email": "id.enim.Curabitur@nonummy.net",
            "web_site": "https://www.Macy.com",
            "city_id": 13,
            "type": "general",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "rejected",
			"published": False,

            "geo_location": "-1.52048, -20.0232"
        },
        {
            "name": "Jack Valdez",
            "address": "272 Luctus Ave",
            "phone": "(663) 771-7716",
            "email": "iaculis.aliquet@enimnon.org",
            "web_site": "https://www.Stephanie.com",
            "city_id": 10,
            "type": "general",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "rejected",
			"published": False,

            "geo_location": "46.90089, 77.911"
        },
        {
            "name": "Ulysses Crosby",
            "address": "P.O. Box 567, 1943 Vulputate, Rd.",
            "phone": "(900) 757-7868",
            "email": "Nullam@loremeu.ca",
            "web_site": "https://www.Eve.com",
            "city_id": 14,
            "type": "general",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "rejected",
			"published": False,

            "geo_location": "-18.77066, 85.02954"
        },
        {
            "name": "Ulysses Moses",
            "address": "Ap #587-6621 Congue St.",
            "phone": "(354) 127-1087",
            "email": "augue.id@aliquamenim.edu",
            "web_site": "https://www.Joelle.com",
            "city_id": 4,
            "type": "general",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "rejected",
			"published": False,

            "geo_location": "-53.14448, -39.41993"
        },
        {
            "name": "Benjamin Whitehead",
            "address": "Ap #397-2368 Libero. St.",
            "phone": "(585) 439-9387",
            "email": "tempor@Pellentesqueultriciesdignissim.co.uk",
            "web_site": "https://www.Maxine.com",
            "city_id": 23,
            "type": "general",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "rejected",
			"published": False,

            "geo_location": "-0.30826, -26.62818"
        },
        {
            "name": "George Morrison",
            "address": "963-9732 Vehicula. Road",
            "phone": "(992) 266-0632",
            "email": "pede.ac.urna@convallisligula.co.uk",
            "web_site": "https://www.Hadassah.com",
            "city_id": 10,
            "type": "salud",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "approved",
			"published": True,

            "geo_location": "72.85296, -37.94386"
        },
        {
            "name": "Neil Keller",
            "address": "4099 Nec, Road",
            "phone": "(114) 425-9123",
            "email": "quam.elementum.at@Nullatemporaugue.com",
            "web_site": "https://www.Jaquelyn.com",
            "city_id": 1,
            "type": "salud",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "approved",
			"published": True,

            "geo_location": "-52.75021, 56.39467"
        },
        {
            "name": "Bruce Robertson",
            "address": "270-8194 Leo, St.",
            "phone": "(719) 146-3109",
            "email": "dolor@varius.com",
            "web_site": "https://www.Leila.com",
            "city_id": 14,
            "type": "salud",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "approved",
			"published": True,

            "geo_location": "-57.35384, -96.19838"
        },
        {
            "name": "Randall Mendoza",
            "address": "425-6669 Morbi Ave",
            "phone": "(775) 349-6059",
            "email": "nonummy@commodo.org",
            "web_site": "https://www.Blythe.com",
            "city_id": 24,
            "type": "salud",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "approved",
			"published": True,

            "geo_location": "-83.85124, 48.28826"
        },
        {
            "name": "Griffin Chapman",
            "address": "6054 Dictum. Rd.",
            "phone": "(505) 536-2311",
            "email": "iaculis@fringillamilacinia.net",
            "web_site": "https://www.Lisandra.com",
            "city_id": 21,
            "type": "salud",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "approved",
			"published": True,

            "geo_location": "64.14131, -5.45627"
        },
        {
            "name": "Chaney Deleon",
            "address": "984-4812 Risus. Street",
            "phone": "(646) 595-9267",
            "email": "erat.Etiam.vestibulum@semegestasblandit.org",
            "web_site": "https://www.Ila.com",
            "city_id": 22,
            "type": "salud",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "approved",
			"published": True,

            "geo_location": "39.49738, -62.82087"
        },
        {
            "name": "Graham Lamb",
            "address": "Ap #801-507 Fringilla Road",
            "phone": "(656) 743-6786",
            "email": "Nunc@suscipit.org",
            "web_site": "https://www.Fay.com",
            "city_id": 20,
            "type": "salud",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "approved",
			"published": True,

            "geo_location": "28.70681, 169.15634"
        },
        {
            "name": "Alec Holmes",
            "address": "Ap #313-7961 Pretium Rd.",
            "phone": "(840) 524-3972",
            "email": "arcu.Vestibulum.ante@vulputate.ca",
            "web_site": "https://www.Melissa.com",
            "city_id": 23,
            "type": "salud",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "approved",
			"published": True,

            "geo_location": "66.44082, 61.57636"
        },
        {
            "name": "Shad Doyle",
            "address": "721-651 Lorem Ave",
            "phone": "(546) 296-5554",
            "email": "Pellentesque@nullaIn.edu",
            "web_site": "https://www.Libby.com",
            "city_id": 19,
            "type": "salud",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "approved",
			"published": True,

            "geo_location": "56.85814, -44.87736"
        },
        {
            "name": "Holmes Simon",
            "address": "1064 In, St.",
            "phone": "(506) 363-0445",
            "email": "cursus@tincidunt.edu",
            "web_site": "https://www.Jena.com",
            "city_id": 17,
            "type": "salud",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "approved",
			"published": False,

            "geo_location": "-50.79657, 34.90389"
        },
        {
            "name": "Stewart Galloway",
            "address": "544-6293 Sagittis Rd.",
            "phone": "(387) 135-8923",
            "email": "in.aliquet@vel.co.uk",
            "web_site": "https://www.Myra.com",
            "city_id": 3,
            "type": "salud",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "approved",
			"published": False,

            "geo_location": "-32.10208, 166.09958"
        },
        {
            "name": "Dillon Norton",
            "address": "P.O. Box 412, 6818 Aliquam Street",
            "phone": "(575) 311-2066",
            "email": "laoreet.posuere@et.co.uk",
            "web_site": "https://www.Yen.com",
            "city_id": 26,
            "type": "salud",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "approved",
			"published": False,

            "geo_location": "-27.26932, 13.91126"
        },
        {
            "name": "Louis Huber",
            "address": "Ap #757-5651 Mi Av.",
            "phone": "(556) 200-4039",
            "email": "lorem@sitametlorem.edu",
            "web_site": "https://www.Emi.com",
            "city_id": 28,
            "type": "salud",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "approved",
			"published": False,

            "geo_location": "72.62085, -65.55914"
        },
        {
            "name": "Keith Pitts",
            "address": "Ap #688-5964 Odio. Av.",
            "phone": "(978) 668-8189",
            "email": "tincidunt.vehicula@nunc.co.uk",
            "web_site": "https://www.MacKensie.com",
            "city_id": 17,
            "type": "salud",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "approved",
			"published": False,

            "geo_location": "-67.93376, 115.31118"
        },
        {
            "name": "Harrison Mckinney",
            "address": "3162 Sed Rd.",
            "phone": "(558) 582-1847",
            "email": "Quisque@tempus.com",
            "web_site": "https://www.Emily.com",
            "city_id": 20,
            "type": "salud",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "approved",
			"published": False,

            "geo_location": "-17.03772, 146.64229"
        },
        {
            "name": "Beck Pennington",
            "address": "753-9145 Rhoncus Rd.",
            "phone": "(707) 591-8954",
            "email": "libero.Donec@malesuada.co.uk",
            "web_site": "https://www.Leila.com",
            "city_id": 9,
            "type": "salud",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "approved",
			"published": False,

            "geo_location": "68.12259, -46.48113"
        },
        {
            "name": "Harlan Coleman",
            "address": "P.O. Box 449, 8886 Lacus. Rd.",
            "phone": "(833) 864-0003",
            "email": "Proin@rutrumlorem.ca",
            "web_site": "https://www.Gemma.com",
            "city_id": 12,
            "type": "salud",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "approved",
			"published": False,

            "geo_location": "22.99388, -159.03609"
        },
        {
            "name": "Fulton Neal",
            "address": "P.O. Box 985, 9008 Ornare, Ave",
            "phone": "(533) 170-2521",
            "email": "ante.iaculis.nec@orci.co.uk",
            "web_site": "https://www.Ria.com",
            "city_id": 6,
            "type": "salud",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "approved",
			"published": False,

            "geo_location": "84.78805, 52.44064"
        },
        {
            "name": "Tate Ramsey",
            "address": "P.O. Box 787, 3079 Eu Street",
            "phone": "(890) 949-3189",
            "email": "dictum@eratvelpede.co.uk",
            "web_site": "https://www.Callie.com",
            "city_id": 21,
            "type": "salud",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "approved",
			"published": False,

            "geo_location": "29.23232, -106.85368"
        },
        {
            "name": "Harlan Mcpherson",
            "address": "119-328 Ullamcorper. Av.",
            "phone": "(609) 856-5446",
            "email": "orci.in.consequat@Pellentesqueultriciesdignissim.org",
            "web_site": "https://www.Iliana.com",
            "city_id": 13,
            "type": "salud",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "approved",
			"published": False,

            "geo_location": "-48.92283, -75.10375"
        },
        {
            "name": "Mufutau Doyle",
            "address": "P.O. Box 424, 8174 Consequat Av.",
            "phone": "(453) 179-3217",
            "email": "auctor@pharetraNamac.ca",
            "web_site": "https://www.Charity.com",
            "city_id": 8,
            "type": "salud",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "approved",
			"published": False,

            "geo_location": "20.93141, -129.80747"
        },
        {
            "name": "Harlan Stark",
            "address": "Ap #910-4250 Sem St.",
            "phone": "(784) 555-7169",
            "email": "auctor.velit@duiquisaccumsan.net",
            "web_site": "https://www.Lois.com",
            "city_id": 14,
            "type": "salud",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "approved",
			"published": False,

            "geo_location": "-3.26106, -111.83292"
        },
        {
            "name": "Kennan Leon",
            "address": "2895 Dui St.",
            "phone": "(456) 121-0387",
            "email": "eu@estcongue.edu",
            "web_site": "https://www.Odette.com",
            "city_id": 25,
            "type": "salud",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "approved",
			"published": False,

            "geo_location": "-35.48654, 173.953"
        },
        {
            "name": "Thane Bond",
            "address": "5990 Eget St.",
            "phone": "(607) 617-6256",
            "email": "nec.mollis.vitae@fermentumconvallisligula.edu",
            "web_site": "https://www.Alma.com",
            "city_id": 22,
            "type": "salud",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "approved",
			"published": False,

            "geo_location": "51.39711, 161.95409"
        },
        {
            "name": "Hasad Hall",
            "address": "P.O. Box 549, 5000 Dolor Rd.",
            "phone": "(808) 633-8117",
            "email": "inceptos.hymenaeos.Mauris@euarcu.edu",
            "web_site": "https://www.Piper.com",
            "city_id": 11,
            "type": "salud",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "approved",
			"published": False,

            "geo_location": "-74.16089, 37.47218"
        },
        {
            "name": "Ivor Olsen",
            "address": "Ap #831-1716 Lobortis, Rd.",
            "phone": "(542) 991-6786",
            "email": "Praesent.interdum.ligula@aliquet.ca",
            "web_site": "https://www.Alice.com",
            "city_id": 3,
            "type": "salud",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "approved",
			"published": False,

            "geo_location": "-50.29322, 153.77538"
        },
        {
            "name": "Nehru Zamora",
            "address": "P.O. Box 229, 3897 Eleifend Rd.",
            "phone": "(209) 278-1536",
            "email": "Nullam.scelerisque.neque@etnetus.net",
            "web_site": "https://www.Dahlia.com",
            "city_id": 23,
            "type": "salud",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "approved",
			"published": False,

            "geo_location": "-14.79298, 86.62935"
        },
        {
            "name": "Bradley Larsen",
            "address": "Ap #832-9695 Ut Street",
            "phone": "(365) 741-3954",
            "email": "consectetuer@sedfacilisisvitae.net",
            "web_site": "https://www.Mara.com",
            "city_id": 29,
            "type": "salud",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "approved",
			"published": False,

            "geo_location": "-32.75646, -65.31224"
        },
        {
            "name": "Russell Hood",
            "address": "P.O. Box 288, 9126 Hendrerit Avenue",
            "phone": "(659) 898-7991",
            "email": "a.feugiat.tellus@tellus.co.uk",
            "web_site": "https://www.Jordan.com",
            "city_id": 10,
            "type": "salud",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "approved",
			"published": False,

            "geo_location": "76.14129, 67.63632"
        },
        {
            "name": "Hayden Mcgee",
            "address": "P.O. Box 479, 4762 Congue St.",
            "phone": "(205) 188-3982",
            "email": "elit.pretium@temporarcu.org",
            "web_site": "https://www.Cameran.com",
            "city_id": 17,
            "type": "salud",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "approved",
			"published": False,

            "geo_location": "32.54869, -87.66695"
        },
        {
            "name": "Steven Delacruz",
            "address": "P.O. Box 285, 1992 Est. Rd.",
            "phone": "(260) 208-1034",
            "email": "libero.mauris.aliquam@consequat.com",
            "web_site": "https://www.Brianna.com",
            "city_id": 18,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "-42.26103, -34.23717"
        },
        {
            "name": "Henry Knowles",
            "address": "Ap #997-8191 Magna. St.",
            "phone": "(913) 866-3968",
            "email": "Integer.id.magna@utnullaCras.edu",
            "web_site": "https://www.Lynn.com",
            "city_id": 13,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "32.27731, -113.08469"
        },
        {
            "name": "Hyatt Dalton",
            "address": "3748 Nunc St.",
            "phone": "(315) 122-1509",
            "email": "vel@Morbi.co.uk",
            "web_site": "https://www.Elizabeth.com",
            "city_id": 10,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "42.7001, -69.12884"
        },
        {
            "name": "Jonah Carrillo",
            "address": "675-5327 At, Road",
            "phone": "(124) 589-1635",
            "email": "dolor@faucibus.org",
            "web_site": "https://www.Lara.com",
            "city_id": 9,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "5.0972, 141.53215"
        },
        {
            "name": "Yuli Levy",
            "address": "9669 Sed Av.",
            "phone": "(262) 564-0011",
            "email": "interdum@orcitinciduntadipiscing.ca",
            "web_site": "https://www.Maggie.com",
            "city_id": 15,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "68.64176, 10.56924"
        },
        {
            "name": "Kareem Farley",
            "address": "147-3652 Risus. Street",
            "phone": "(575) 178-8835",
            "email": "neque.sed.dictum@consectetuermauris.com",
            "web_site": "https://www.Libby.com",
            "city_id": 13,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "-16.99769, -28.54151"
        },
        {
            "name": "Mufutau Norton",
            "address": "689-3716 Donec Street",
            "phone": "(419) 276-2228",
            "email": "facilisis.non@ligula.co.uk",
            "web_site": "https://www.Mariko.com",
            "city_id": 25,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "77.84556, -138.28887"
        },
        {
            "name": "Cain Terrell",
            "address": "P.O. Box 337, 4775 Luctus Road",
            "phone": "(718) 164-1769",
            "email": "enim.Nunc.ut@estarcuac.ca",
            "web_site": "https://www.MacKenzie.com",
            "city_id": 19,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "-22.16088, -144.92666"
        },
        {
            "name": "Tyler Roth",
            "address": "7313 Egestas Street",
            "phone": "(605) 630-0246",
            "email": "lacus.Etiam@arcuNuncmauris.ca",
            "web_site": "https://www.Jacqueline.com",
            "city_id": 12,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "81.67126, -129.88043"
        },
        {
            "name": "Coby Gould",
            "address": "Ap #834-573 Augue St.",
            "phone": "(442) 526-5424",
            "email": "adipiscing@habitant.net",
            "web_site": "https://www.Gwendolyn.com",
            "city_id": 27,
            "type": "alimentos",
            "opening": "09:00:00",
            "closing": "16:00:00",
            "state": "pending",
			"published": False,

            "geo_location": "-82.6036, 76.94164"
        }
    ]

    for center in centers:
        lat, long = center['geo_location'].replace(' ', '').split(',')
        del center['geo_location']
        center['gl_lat'] = lat
        center['gl_long'] = long

    op.bulk_insert(centers_table, centers)


def downgrade():
    op.drop_table('centers')
    op.drop_table('city')
