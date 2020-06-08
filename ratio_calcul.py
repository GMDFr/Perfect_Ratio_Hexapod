import numpy as np
import math


class ATHLETE(object):
	def __init__(self,L1,L2,L3,ratio1,ratio2,ratio3,body_long,body_larg,body_h,body_mass):
		super(ATHLETE, self).__init__()
		self.L1 = 175 # Coxa
		self.L2 = 673 # Femur
		self.L3 = 447 # Tibia
		self.Leg = (self.L1+self.L2+self.L3)
		self.ratio1 = 0.135
		self.ratio2 = 0.52
		self.ratio3 = 0.345
		self.body_long = 4000
		self.body_larg = 4000
		self.body_h = None
		self.body_mass = 850
	
	def calculate_ratio_segment_leg(L1,L2,L3, ratio1,ratio2, ratio3, body_long, body_larg, body_h, body_mass):
		ratio_Leg_L1 = self.L1/(self.Leg)
		ratio_Leg_L2 = 
		ratio_Leg_L3 = 
		ratio_Leg = [ratio_Leg_L1, ratio_Leg_L2, ratio_Leg_L3]
		return ratio_Leg
		print ratio_Leg

class perfect_ratio_flexibility(object):
 	"""docstring for perfect_ratio"""
 	def __init__(self, arg):
 		super(perfect_ratio, self).__init__()
 		self.arg = arg
 		 0.05,0.3,0.65
	def compare_ratio():
		# comparer deux valeurs de ratios
		#  

		return
		print
		pass



	def calculate_ration_leg_body()
	# (Longueur du corps / 3) 
		ratio_Leg_Body_Hauteur = self.L3/self.body_h
		return ratio_Leg_Body_Hauteur
		print ratio_Leg_Body_Hauteur
		pass
#masse totale
#taille en mm et poids en Kg

class COMET_IV(object):
	def __init__(self,L1,L2,L3,ratio1,ratio2,ratio3,body_long,body_larg,body_h,body_mass):
		super(COMET_IV, self).__init__()
		self.L1 = 0
		self.L2 = 1130
		self.L3 = 770
		self.ratio1 = 0
		self.ratio2 = 0.595
		self.ratio3 = 0.405
		self.body_long = 2500
		self.body_larg = 3300
		self.body_h = 2800
		self.body_mass = 2120
#masse totale
#taille en mm et poids en Kg
#hauteur totale

class SILO6(object):
	def __init__(self,L1,L2,L3,ratio1,ratio2,ratio3,body_long,body_larg,body_h,body_mass):
		super(SILO6, self).__init__()
		self.L1 = 84
		self.L2 = 250
		self.L3 = 250
		self.ratio1 = 0.144
		self.ratio2 = 0.428
		self.ratio3 = 0.428
		self.body_long = 880
		self.body_larg =630
		self.body_h =260
		self.body_mass = 28.2
#taille en mm et poids en Kg
#hauteur totale

class HyQ(object):
	def __init__(self,L1,L2,L3,ratio1,ratio2,ratio3,body_long,body_larg,body_h,body_mass):
		super(HyQ, self).__init__()
		self.L1 = 84
		self.L2 = 350
		self.L3 = 350
		self.ratio1 = 0.102
		self.ratio2 = 0.449
		self.ratio3 = 0.449
		self.body_long = 1000
		self.body_larg =500
		self.body_h =980
		self.body_mass = 90
#taille en mm et poids en Kg
#hauteur totale
#masse totale avec batterie integrée

class TITAN_XI(object):
	def __init__(self,L1,L2,L3,ratio1,ratio2,ratio3,body_long,body_larg,body_h,body_mass):
		super(TITAN_XI, self).__init__()
		self.L1 = 0
		self.L2 = 1900
		self.L3 = 1800
		self.ratio1 = 0
		self.ratio2 = 0.5153
		self.ratio3 = 0.4865
		self.body_long = 5000
		self.body_larg = 4800
		self.body_h = 3000
		self.body_mass = 6800
#taille en mm et poids en Kg
#masse totale
#hauteur totale