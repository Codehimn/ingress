
if accion=='a_enlaza_depto_sp':

	Madisa=MadisaNet()

	cod_fam = Madisa.DirMadisaNet

	error(cl,'No existe registro '  + str(cod_fam))


	#prog_dir = str ( os.environ['ProgramFiles'] )
	prog_dir  =  'C:\\Program Files'	
	madicustno = '99999'
	compno = '1'
	
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
				f = open(prog_dir + '\\MADISA\\MadisaNet\\department.txt','a')
				f.write(datos + '\n')
				f.flush()
				f.close()
			except:
				error(cl,'Error grabacion departamentos en MadisaNet')

		else:
			error(cl,'No existe registro '  + str(cod_fam))

	shutil.move(prog_dir + '\\MADISA\\MadisaNet\\department.txt', prog_dir + '\\MADISA\\MadisaNet\\import\\')
	envia(cl,'OK')
