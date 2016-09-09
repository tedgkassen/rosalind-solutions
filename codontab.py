STANDARD_CODON_TABLE = {
	'TTT' : 'F',
	'TCT' : 'S',
	'TAT' : 'Y',
	'TGT' : 'C',
	'TTC' : 'F',
	'TCC' : 'S',
	'TAC' : 'Y',
	'TGC' : 'C',
	'TTA' : 'L',
	'TCA' : 'S',
	'TAA' : '*',
	'TGA' : '*',
	'TTG' : 'L',
	'TCG' : 'S',
	'TAG' : '*',
	'TGG' : 'W',
	'CTT' : 'L',
	'CCT' : 'P',
	'CAT' : 'H',
	'CGT' : 'R',
	'CTC' : 'L',
	'CCC' : 'P',
	'CAC' : 'H',
	'CGC' : 'R',
	'CTA' : 'L',
	'CCA' : 'P',
	'CAA' : 'Q',
	'CGA' : 'R',
	'CTG' : 'L',
	'CCG' : 'P',
	'CAG' : 'Q',
	'CGG' : 'R',
	'ATT' : 'I',
	'ACT' : 'T',
	'AAT' : 'N',
	'AGT' : 'S',
	'ATC' : 'I',
	'ACC' : 'T',
	'AAC' : 'N',
	'AGC' : 'S',
	'ATA' : 'I',
	'ACA' : 'T',
	'AAA' : 'K',
	'AGA' : 'R',
	'ATG' : 'M',
	'ACG' : 'T',
	'AAG' : 'K',
	'AGG' : 'R',
	'GTT' : 'V',
	'GCT' : 'A',
	'GAT' : 'D',
	'GGT' : 'G',
	'GTC' : 'V',
	'GCC' : 'A',
	'GAC' : 'D',
	'GGC' : 'G',
	'GTA' : 'V',
	'GCA' : 'A',
	'GAA' : 'E',
	'GGA' : 'G',
	'GTG' : 'V',
	'GCG' : 'A',
	'GAG' : 'E',
	'GGG' : 'G'
}

set([('AAA', 'N'), ('AGA', 'S'), ('AGG', 'S'), ('TAA', 'Y'), ('TGA', 'W')])

TABLE_DIFFS = [
	set([]),
	set([]),
	set([('AGA', '*'), 	#transl_table=2
 	     ('AGG', '*'),
 	     ('ATA', 'M'),
 	     ('TGA', 'W')]),
	set([('ATA', 'M'),	#transl_table=3
 	     ('CTT', 'T'),
 	     ('CTC', 'T'),
             ('CTA', 'T'),
             ('CTG', 'T'),
             ('TGA', 'W'),
             ('CGA', None),
             ('CGC', None)]),
	set([('TGA', 'W')]),	#transl_table=4
	set([('AGA', 'S'),     #transl_table=5
 	     ('AGG', 'S'),
             ('ATA', 'M'),
             ('TGA', 'W')]),
	set([('TAA', 'Q'),	#transl_table=6
 	     ('TAG', 'Q')]),
	set([]),		#transl_table=7
	set([]),		#transl_table=8
	set([('AAA', 'N'),	#transl_table=9
             ('AGA', 'S'),
             ('AGG', 'S'),
             ('TGA', 'W')]),
	set([('TGA', 'C')]),	#transl_table=10
	set([]),		#transl_table=11
	set([('CTG', '*')]),	#transl_table=12
	set([('AGA', 'G'),     #transl_table=13
 	     ('AGG', 'G'),
             ('ATA', 'M'),
             ('TGA', 'W')]),
	set([('AAA', 'N'),     #transl_table=14
 	     ('AGA', 'S'),
             ('AGG', 'S'),
	     ('TAA', 'Y'),
             ('TGA', 'W')]),
	set([('TAG', 'Q')])   #transl_table=15
]
