import bottle
import sqlite3

bottle.debug(True)
datoteka_baze = "fejsbuk.sqlite"

############################

@bottle.route('/prijatelji/<id>')
@bottle.view('prijatelji')
def index(id):
    c = baza.cursor()
    c.execute("""SELECT ime, priimek FROM osebe WHERE id = ?""", [id])
    oseba = c.fetchone()
    if oseba is None:
        c.close()
        return {'obstaja': False}
    else:
        (ime, priimek) = oseba
        c.execute(
        """SELECT osebe.ime, osebe.priimek FROM
           osebe JOIN prijateljstva ON osebe.id = prijateljstva.drugi
            WHERE prijateljstva.prvi = ?""", [id])
        prijatelji = c.fetchall()
        c.close()
        return {'obstaja': True, 'ime': ime, 'priimek': priimek, 'prijatelji': prijatelji}


############################

baza = sqlite3.connect(datoteka_baze, isolation_level=None)

bottle.run(host='localhost', port=8080)
    
