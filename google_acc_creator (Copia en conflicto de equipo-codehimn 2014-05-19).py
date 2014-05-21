
if accion=='a_enlaza_depto_sp':

	madisa=MadisaNet()

	cod_fam = Madisa.dir_madisanet

	# error(cl,'No existe registro '  + str(cod_fam))


	#prog_dir = str ( os.environ['ProgramFiles'] )
	prog_dir  =  'C:\\Program Files'	
	madicustno = madisa.madicustno
	compno = madisa.compno
	
	fams=selec(gpx,'familias',['0'])
	nt = len(fams)
	nr = 0
	for cod_fam in fams:
		nr += 1
		if nr % 100 == 0:
			informa(cl,nr,nt,'Exportando','s');
		fam = lee(cl,gpx,'familias',cod_fam)
		fdeno = fam<FM_DENO>
		if fam <> 1:
			datos = madicustno + '|' + compno + '|'	
			datos = datos + cod_fam + '|'
			datos = datos + fdeno + '|'
			datos = datos + '1|'				# todos a la familia 1
			datos = datos + '2|'				# Iva (da igual porque va por articulo)
			datos = datos + '1|0||||0||||0|0||||0|1||'

			try:
				f = open(madisa.dir_import + 'department.txt','a')
				f.write(datos + '\n')
				f.flush()
				f.close()
			except:
				error(cl,'Error grabacion departamentos en MadisaNet')

		else:
			error(cl,'No existe registro '  + str(cod_fam))

	shutil.move(madisa.dir_import + 'department.txt', madisa.dir_import)
	envia(cl,'OK')
