# REQUIREMENTS:
# py -m pip install clipboard


import os        # Used to clear the screen
import time      # Used for the sleep function
import pyperclip # Used to copy the output to your clipboard
from getpass import getpass   # Used to create an invisible input


################################################################################################################
#                                                 GET T2E + T2D                                                #
################################################################################################################
def T2E(): # Text 2 Encrypt function
	global text_raw, text_raw_backup
	text_raw = input('\033[1;36mText to encrypt: \033[1;33m') # Get the text to encrypt from the user
	if len(text_raw) <= 0 or text_raw.isspace() == True:
		T2E() # Return
	text_raw_backup = text_raw # Get a backup of 'text_raw'


def T2D(): # Text 2 Decrypt function
	global text_raw, text_raw_backup
	text_raw = input('\033[1;36mEncrypted text: \033[1;33m') # Get the encrypted text from the user
	if len(text_raw) <= 0 or text_raw.isspace() == True:
		T2D() # Return
	text_raw_backup = text_raw # Get a backup of 'text_raw'



################################################################################################################
#                                       MAIN FUNCTION OF THE CIPHER TOOL                                       #
################################################################################################################
def Main():
	global use_lang, text_raw, text_raw_backup
	os.system('mode 57,20 && title Cipher Tool ~ By: 0xifer && cls')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	print('       \033[1;31m╔═════════════════════\033[1;36m═══════════════════╗')
	print('       \033[1;31m║           -WELCOME T\033[1;36mO CIPHER-          ║')
	print('       \033[1;31m║        ╔════════════\033[1;36m═══════════╗       \033[1;36m║')
	print('       \033[1;31m╠════════╣  ENTER \033[1;33m"H"\033[1;36m  FOR HELP  ╠═══════╣')
	print('       \033[1;31m║        ╚════════════\033[1;36m═══════════╝       \033[1;36m║')
	print('       \033[1;31m║ TYPE \033[1;33m"CMD" \033[1;31mAND VIEW  \033[1;36mLIST OF COMMANDS  ║')
	print('       \033[1;31m╚═════════════════════\033[1;36m═══════════════════╝')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;0m')
	use_lang = input('\033[1;36mAlphabet \033[1;31m/ \033[1;36mGoto: \033[1;33m').lower() # Request alphabet/goto from the user
################################################################################################################
#                                   FIND WHAT LANGUAGE AND RUN THAT FUNCTION                                   #
################################################################################################################
	if use_lang == 'r':
		Reverse()
	if use_lang == 'se':
		S_ENCRYPT()
	if use_lang == 'sd':
		S_DECRYPT()
	if use_lang == 'ae':
		A_ENCRYPT()
	if use_lang == 'ad':
		A_DECRYPT()
	if use_lang == 'e':
		N_ENCRYPT()
	if use_lang == 'd':
		N_DECRYPT()
	if use_lang == 'mt':
		MT()
	if use_lang == 'rmt':
		RMT()
	if use_lang == 'alg':
		ALG()
	if use_lang == 'h':
		HELP4USER()
		Main()
	if use_lang == 'cmd':
		cmds()
		Main()
	if use_lang == 'l':
		list_langs()
		Main()
	if use_lang == 'rya':
		T2E()
		lang_rya()
		Output()
		Main()
	if use_lang == 'lazy':
		T2E()
		lang_lazy()
		Output()
		Main()
	if use_lang == '0x':
		T2E()
		lang_0x()
		Output()
		Main()
	if use_lang == '0xq':
		T2E()
		lang_0xq()
		Output()
		Main()
	if use_lang == 'leet':
		lang_leet()
		T2E()
		lang_leet2()
		Output()
		Main()
	if use_lang == 'binary':
		T2E()
		lang_binary()
		Output()
		Main()
	if use_lang == 'crazy':
		T2E()
		lang_crazy()
		Output()
		Main()
	if use_lang == 'crazy2':
		T2E()
		lang_crazy2()
		Output()
		Main()
	if use_lang == 'bw':
		T2E()
		lang_backwards()
		Output()
		Main()
	if use_lang == '3r':
		T2E()
		lang_3R()
		Output()
		Main()
	if use_lang == '3l':
		T2E()
		lang_3L()
		Output()
		Main()
	if use_lang == '2r':
		T2E()
		lang_2R()
		Output()
		Main()
	if use_lang == '2l':
		T2E()
		lang_2L()
		Output()
		Main()
	if use_lang == '1r':
		T2E()
		lang_1R()
		Output()
		Main()
	if use_lang == '1l':
		T2E()
		lang_1L()
		Output()
		Main()
	if use_lang == 'uc':
		T2E()
		lang_UC()
		Output()
		Main()
	if use_lang == 'lc':
		T2E()
		lang_LC()
		Output()
		Main()
	if use_lang == 'vr':
		lang_VR()
		Output()
		Main()

	INV_OPT() # Invalid Option
	Main() # Return

################################################################################################################
#                                                   REVERSE                                                    #
################################################################################################################
def Reverse():
	os.system('mode 57,23 && title Reverse && cls')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	print('                  \033[1;33m╔══════════════════╗')
	print('        ╔═════════╣\033[1;31mWelcome to Reverse\033[1;33m╠═════════╗')
	print('        ║         ╚══════════════════╝         ║')
	print('        ║\033[1;33m1. \033[1;36mEnter the alphabet to decrypt from \033[1;33m║')
	print('        ║      \033[1;33m2. \033[1;36mEnter the encrypted text     \033[1;33m║')
	print('        ║         \033[1;31mENTER \033[1;33m"B" \033[1;31mTO GO BACK         \033[1;33m║')
	print('        ║ ╔══════════════════════════════════╗ ║')
	print('        ╚═╣\033[1;35mTo see preset languages, enter \033[1;33m"L"\033[1;33m╠═╝')
	print('          ╚══════════════════════════════════╝')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	R_use_lang = input('\033[1;36mAlphabet: \033[1;33m').lower()
	if R_use_lang == 'b':
		Main()
	if R_use_lang == 'l':
		list_langs()
		Reverse()
	if R_use_lang == 'rya':
		T2D()
		lang_rya()
		Output()
		Reverse()
	if R_use_lang == 'lazy':
		T2D()
		lang_lazy()
		Output()
		Reverse()
	if R_use_lang == '0x':
		T2D()
		lang_R_0x()
		Output()
		Reverse()
	if R_use_lang == '0xq':
		T2D()
		lang_R_0xq()
		Output()
		Reverse()
	if R_use_lang == 'leet':
		lang_leet()
		T2D()
		lang_R_leet2()
		Output()
		Reverse()
	if R_use_lang == 'binary':
		T2D()
		lang_R_binary()
		Output()
		Reverse()
	if R_use_lang == 'crazy':
		T2D()
		lang_R_crazy()
		Output()
		Reverse()
	if R_use_lang == 'crazy2':
		T2D()
		lang_R_crazy2()
		Output()
		Reverse()
	if R_use_lang == 'bw':
		T2D()
		lang_backwards()
		Output()
		Reverse()
	if R_use_lang == '3r':
		T2D()
		lang_3L()
		Output()
		Reverse()
	if R_use_lang == '3l':
		T2D()
		lang_3R()
		Output()
		Reverse()
	if R_use_lang == '2r':
		T2D()
		lang_2L()
		Output()
		Reverse()
	if R_use_lang == '2r':
		T2D()
		lang_2R()
		Output()
		Reverse()
	if R_use_lang == '1r':
		T2D()
		lang_1L()
		Output()
		Reverse()
	if R_use_lang == '1l':
		T2D()
		lang_1R()
		Output()
		Reverse()
	if R_use_lang == 'uc':
		T2D()
		lang_LC()
		Output()
		Reverse()
	if R_use_lang == 'lc':
		T2D()
		lang_UC()
		Output()
		Reverse()

	INV_OPT()
	Reverse()

################################################################################################################
#                         OUTPUT FOR ENCRYPTED TEXT / SAVING OUTPUT FOR ENCRYPTED TEXT                         #
################################################################################################################
def Output():
	global use_lang, text_raw, text_raw_backup
	os.system('mode 57,20 && title Output && cls')
	print('	   \033[1;31m╔═══════════════════\033[1;36m════════════════╗')
	print('	   \033[1;31m║        CIPHERED TE\033[1;36mXT BELOW        ║')
	print('	   \033[1;31m╚═══════════════════\033[1;36m════════════════╝')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	print('\n\033[1;33m' + text_raw + '\n')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	output_options = input('\033[1;33m"C" \033[1;36m= COPY \033[1;31m/ \033[1;33m"S" \033[1;35m= SAVE: \033[1;33m').lower()
	if len(output_options) <= 0 or output_options.isspace() == True:
		Output()
################################################################################################################
#                                                  COPY OUTPUT                                                 #
################################################################################################################
	if output_options == 'c':
		try: 
			pyperclip.copy(text_raw)
		except:
			print('\033[1;31mTHERE WAS AN ERROR COPYING THE TEXT')
			time.sleep(1)
			Output()
		else:
			print('                         \033[1;36m╔════════╗')
			print('	                 ║ \033[1;33mCOPIED \033[1;36m║')
			print('	                 ╚════════╝')
			time.sleep(.7) # Wait
################################################################################################################
#                                                  SAVE OUTPUT                                                 #
################################################################################################################
	if output_options == 's':
		def Ask4FileName():
			global save_output_A_name
			save_output_A_name = input('\033[1;36mEnter the name for this file: \033[1;33m')
			if len(save_output_A_name) <= 0 or save_output_A_name.isspace() == True:
				Ask4FileName()
		print('\n                \033[1;31m╔═════════\033[1;36m═════════╗')
		print('       \033[1;31m╔════════╣ CHOOSE A\033[1;36mN OPTION ╠════════╗')
		print('       \033[1;31m║        ╚═════════\033[1;36m═════════╝        ║')
		print('       \033[1;31m║    \033[1;33mR \033[1;31m= \033[1;36mReplace / Create TXT file   ║')
		print('       \033[1;31m║       \033[1;33mA \033[1;31m= \033[1;36mAdd / Create TXT file    ║')
		print('       \033[1;31m╚══════════════════\033[1;36m══════════════════╝')
		save_output = input('\033[1;36mEnter option \033[1;33m"R" \033[1;31m/ \033[1;33m"A"\033[1;36m: \033[1;33m').lower() # Ask user if they wanna replace the text file or add on to a txt file
		if len(save_output) <= 0 or save_output.isspace() == True:
			INV_OPT()
			Output()
		if save_output == "r":
			Ask4FileName()
			SO_R_N = open(save_output_R_name, 'w')
			print('\n    \033[1;35m╔════════════════════════════════════════╗')
			print('    ║    \033[1;33mDo you want to add labels for the   \033[1;35m║')
			print('    ║          \033[1;33mlanguage and the text?        \033[1;35m║')
			print('    ╚════════════════════════════════════════╝')
			print('                  \033[1;33mY \033[1;31m= \033[1;36mYes \033[1;31m/ \033[1;33mN \033[1;31m= \033[1;36mNo')
			save_output_R_labels = input('\033[1;36mAdd labels?: \033[1;33m').lower()
			if len(save_output) <= 0 or save_output.isspace() == True:
				INV_OPT()
				Output()
			if save_output_R_labels.startswith('y') == True:
				if use_lang == 'leet':
					print('Input = ' + text_raw_backup + '\nLanguage = ' + use_lang + ' / LEVEL-' + str(leet_level) + '\nOutput = ' + text_raw, file = SO_R_N)
				else:
					print('Input = ' + text_raw_backup + '\nLanguage = ' + use_lang + '\nOutput = ' + text_raw, file = SO_R_N)
			if save_output_R_labels.startswith('n') == True:
				if use_lang == 'leet':
					print(text_raw_backup + '\n' + use_lang + '-' + str(leet_level) + '\n' + text_raw, file = SO_R_N)
				else:
					print(text_raw_backup + '\n' + use_lang + '\n' + text_raw, file = SO_R_N)
			print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
			print('\033[1;31mSuccessfully saved to ' + '\033[1;33m"' + save_output_R_name)
			print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
			time.sleep(2) # Wait
		if save_output == "a":
			Ask4FileName()
			SO_A_N = open(save_output_A_name, 'a')
			print('\n \033[1;35m╔═══════════════════════════════════════════════╗')
			print(' ║ \033[1;33mDo you want to add a header before the output \033[1;35m║')
			print(' ║   \033[1;33minside the TXT file as a way of spotting?   \033[1;35m║')
			print(' ╚═══════════════════════════════════════════════╝')
			print('                  \033[1;33mY \033[1;31m= \033[1;36mYes \033[1;31m/ \033[1;33mN \033[1;31m= \033[1;36mNo')
			save_output_A_header = input('\033[1;36mAdd a header?: \033[1;33m').lower()
			if save_output_A_header.startswith('y') == True:
				print('\n    \033[1;35m╔════════════════════════════════════════╗')
				print('    ║    \033[1;33mDo you want to add labels for the   \033[1;35m║')
				print('    ║          \033[1;33mlanguage and the text?        \033[1;35m║')
				print('    ╚════════════════════════════════════════╝')
				print('                 \033[1;33mY \033[1;31m= \033[1;36mYes \033[1;31m/ \033[1;33mN \033[1;31m= \033[1;36mNo')
				save_output_A_header_label = input('\033[1;36mAdd labels?: \033[1;33m').lower()
				if save_output_A_header_label.startswith('y') == True:
					print('#====================================#\n#	     Created by 0xifer	     #\n#====================================#\nInput = ' + text_raw_backup + '\nLanguage = ' + use_lang + '\nOutput = ' + text_raw, file = SO_A_N)
				if save_output_A_header_label.startswith('n') == True:
					print('#====================================#\n#	     Created by 0xifer	     #\n#====================================#\n' + text_raw_backup + '\n' + use_lang + '\n' + text_raw, file = SO_A_N)
			if save_output_A_header.startswith('n') == True:
				print('\n    \033[1;35m╔════════════════════════════════════════╗')
				print('    ║    \033[1;33mDo you want to add labels for the   \033[1;35m║')
				print('    ║          \033[1;33mlanguage and the text?        \033[1;35m║')
				print('    ╚════════════════════════════════════════╝')
				print('                 \033[1;33mY \033[1;31m= \033[1;36mYes \033[1;31m/ \033[1;33mN \033[1;31m= \033[1;36mNo')
				save_output_A_header_label = input('\033[1;36mAdd labels?: \033[1;33m').lower()
				if save_output_A_header_label.startswith('y') == True:
					print('#====================================#\n#	     Created by 0xifer	     #\n#====================================#\nInput = ' + text_raw_backup + '\nLanguage = ' + use_lang + '\nOutput = ' + text_raw, file = SO_A_N) # Print this into the save file
				if save_output_A_header_label.startswith('n') == True:
					print('#====================================#\n#	     Created by 0xifer	     #\n#====================================#\n' + text_raw_backup + '\n' + use_lang + '\n' + text_raw, file = SO_A_N) # Print this into the save file
				print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
				print('\033[1;31mSuccessfully saved to ' + '\033[1;33m"' + save_output_A_name)
				print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
				time.sleep(2) # Wait
################################################################################################################


def ENC_ADD_LABELS():
	print('\n     \033[1;35m╔════════════════════════════════════════╗')
	print('     ║    \033[1;33mDo you want to add labels for the   \033[1;35m║')
	print('     ║         \033[1;33mInput / Code(s) / Output?      \033[1;35m║')
	print('     ╚════════════════════════════════════════╝')
	print('                  \033[1;33mY \033[1;31m= \033[1;36mYes \033[1;31m/ \033[1;33mN \033[1;31m= \033[1;36mNo')
################################################################################################################


def ENC_Output(ENC_USED):
	global text_raw, text_raw_backup, inputcode_1, inputcode_2, inputcode_3, inputcode_4, inputcode_5, inputcode_6, inputcode_7, inputcode_8, inputcode_9, inputcode_10, inputcode_11, inputcode_13, inputcode_14, inputcode_15, inputcode_16, inputcode_17, inputcode_18, inputcode_19, inputcode_20, inputcode_21
	ENC_BACKUP = ENC_USED
	os.system('title Output [Encrypter/Decrypter] && cls')
	print('	   \033[1;31m╔═══════════════════\033[1;36m════════════════╗')
	print('	   \033[1;31m║        CIPHERED TE\033[1;36mXT BELOW        ║')
	print('	   \033[1;31m╚═══════════════════\033[1;36m════════════════╝')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	print('\n\033[1;33m' + text_raw + '\n')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	output_options = input('\033[1;33m"C" \033[1;36m= COPY \033[1;31m/ \033[1;33m"S" \033[1;35m= SAVE: \033[1;33m').lower()
	if len(output_options) <= 0 or output_options.isspace() == True:
		ENC_Output(ENC_BACKUP)
################################################################################################################
#                                                ENC COPY OUTPUT                                               #
################################################################################################################
	if output_options == 'c':
		try: 
			pyperclip.copy(text_raw)
		except:
			print('\033[1;31mTHERE WAS AN ERROR COPYING THE TEXT')
			time.sleep(1)
			ENC_Output()
		else:
			print('                         \033[1;36m╔════════╗')
			print('	                 ║ \033[1;33mCOPIED \033[1;36m║')
			print('	                 ╚════════╝')
			time.sleep(.7) # Wait
################################################################################################################
#                                                ENC SAVE OUTPUT                                               #
################################################################################################################
	if output_options == 's':
		print('\n                \033[1;31m╔═════════\033[1;36m═════════╗')
		print('       \033[1;31m╔════════╣ CHOOSE A\033[1;36mN OPTION ╠════════╗')
		print('       \033[1;31m║        ╚═════════\033[1;36m═════════╝        ║')
		print('       \033[1;31m║    \033[1;33mR \033[1;31m= \033[1;36mReplace / Create TXT file   ║')
		print('       \033[1;31m║       \033[1;33mA \033[1;31m= \033[1;36mAdd / Create TXT file    ║')
		print('       \033[1;31m╚══════════════════\033[1;36m══════════════════╝')
		save_output = input('\033[1;36mEnter option \033[1;33m"R" \033[1;31m/ \033[1;33m"A"\033[1;36m: \033[1;33m').lower() # Ask user if they wanna replace the text file or add on to a txt file

		if save_output == "r":
			save_output_R_name = input('\033[1;36mEnter the name for this file: \033[1;33m') # Get the name of the text file to replace
			SO_R_N = open(save_output_R_name, 'w')
			ENC_ADD_LABELS()
			save_output_R_labels = input('\033[1;36mAdd labels?: \033[1;33m').lower()
			if len(save_output_R_labels) <= 0 or save_output_R_labels.isspace() == True:
				INV_OPT()
				ENC_Output()
			if save_output_R_labels.startswith('y') == True:
				if ENC_USED == 'ne' or ENC_USED == 'nd':
					print('Input = ' + text_raw_backup + '\nSeperator = ' + NE_Seperator + '\n\nCode = ' + str(inputcode_1) + '\n\nOutput = ' + text_raw, file = SO_R_N)
				if ENC_USED == 'ae' or ENC_USED == 'ad':
					print('Input = ' + text_raw_backup + '\nSeperator = ' + AE_Seperator + '\n\nCode #1 = ' + str(inputcode_1) + '\nCode #2 = ' + str(inputcode_2) + '\nCode #3 = ' + str(inputcode_3) + '\nCode #4 = ' + str(inputcode_4) + '\nCode #5 = ' + str(inputcode_5) + '\n\nOutput = ' + text_raw, file = SO_R_N)
				if ENC_USED == 'se' or ENC_USED == 'sd':
					print('Input = ' + text_raw_backup + '\nSeperator = ' + SE_Seperator + '\n\nCode #1 = ' + str(inputcode_1) + '\nCode #2 = ' + str(inputcode_2) + '\nCode #3 = ' + str(inputcode_3) + '\nCode #4 = ' + str(inputcode_4) + '\nCode #5 = ' + str(inputcode_5) + '\nCode #6 = ' + str(inputcode_6) + '\nCode #7 = ' + str(inputcode_7) + '\nCode #8 = ' + str(inputcode_8) + '\nCode #9 = ' + str(inputcode_9) + '\nCode #10 = ' + str(inputcode_10) + '\nCode #11 = ' + str(inputcode_11) + '\nCode #12 = ' + str(inputcode_13) + '\nCode #13 = ' + str(inputcode_14) + '\nCode #14 = ' + str(inputcode_15) + '\nCode #15 = ' + str(inputcode_16) + '\nCode #16 = ' + str(inputcode_17) + '\nCode #17 = ' + str(inputcode_18) + '\nCode #18 = ' + str(inputcode_19) + '\nCode #19 = ' + str(inputcode_20) + '\nCode #20 = ' + str(inputcode_21) + '\n\nOutput = ' + text_raw, file = SO_R_N)
			if save_output_R_labels == "n":
				if ENC_USED == 'ne':
					print(text_raw_backup + '\n' + NE_Seperator + '\n' + str(inputcode_1) + '\n\n' + text_raw, file = SO_R_N)
				if ENC_USED == 'ae':
					print(text_raw_backup + '\n' + AE_Seperator + '\n' + str(inputcode_1) + '\n' + str(inputcode_2) + '\n' + str(inputcode_3) + '\n' + str(inputcode_4) + '\n' + str(inputcode_5) + '\n\n' + text_raw, file = SO_R_N)
				if ENC_USED == 'se':
					print(text_raw_backup + '\n' + SE_Seperator + '\n' + str(inputcode_1) + '\n' + str(inputcode_2) + '\n' + str(inputcode_3) + '\n' + str(inputcode_4) + '\n' + str(inputcode_5) + '\n' + str(inputcode_6) + '\n' + str(inputcode_7) + '\n' + str(inputcode_8) + '\n' + str(inputcode_9) + '\n' + str(inputcode_10) + '\n' + str(inputcode_11) + '\n' + str(inputcode_13) + '\n' + str(inputcode_14) + '\n' + str(inputcode_15) + '\n' + str(inputcode_16) + '\n' + str(inputcode_17) + '\n' + str(inputcode_18) + '\n' + str(inputcode_19) + '\n' + str(inputcode_20) + '\n' + str(inputcode_21) + '\n\n' + text_raw, file = SO_R_N)
				if ENC_USED == 'nd':
					print(text_raw_backup + '\n' + ND_Seperator + '\n' + str(inputcode_1) + '\n\n' + text_raw, file = SO_R_N)
				if ENC_USED == 'ad':
					print(text_raw_backup + '\n' + AD_Seperator + '\n' + str(inputcode_1) + '\n' + str(inputcode_2) + '\n' + str(inputcode_3) + '\n' + str(inputcode_4) + '\n' + str(inputcode_5) + '\n\n' + text_raw, file = SO_R_N)
				if ENC_USED == 'sd':
					print(text_raw_backup + '\n' + SD_Seperator + '\n' + str(inputcode_1) + '\n' + str(inputcode_2) + '\n' + str(inputcode_3) + '\n' + str(inputcode_4) + '\n' + str(inputcode_5) + '\n' + str(inputcode_6) + '\n' + str(inputcode_7) + '\n' + str(inputcode_8) + '\n' + str(inputcode_9) + '\n' + str(inputcode_10) + '\n' + str(inputcode_11) + '\n' + str(inputcode_13) + '\n' + str(inputcode_14) + '\n' + str(inputcode_15) + '\n' + str(inputcode_16) + '\n' + str(inputcode_17) + '\n' + str(inputcode_18) + '\n' + str(inputcode_19) + '\n' + str(inputcode_20) + '\n' + str(inputcode_21) + '\n\n' + text_raw, file = SO_R_N)
			print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
			print('\033[1;31mSuccessfully saved to ' + '\033[1;33m"' + save_output_R_name)
			print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
			time.sleep(2) # Wait

		if save_output == "a":
			save_output_A_name = input('\n\033[1;36mEnter the name for this file: \033[1;33m')
			SO_A_N = open(save_output_A_name, 'a')
			print('\n \033[1;35m╔═══════════════════════════════════════════════╗')
			print(' ║ \033[1;33mDo you want to add a header before the output \033[1;35m║')
			print(' ║   \033[1;33minside the TXT file as a way of spotting?   \033[1;35m║')
			print(' ╚═══════════════════════════════════════════════╝')
			print('                  \033[1;33mY \033[1;31m= \033[1;36mYes \033[1;31m/ \033[1;33mN \033[1;31m= \033[1;36mNo')
			save_output_A_header = input('\033[1;36mAdd a header?: \033[1;33m').lower()
			if save_output_A_header.startswith('y') == True:
				ENC_ADD_LABELS()
				save_output_A_header_label = input('\033[1;36mAdd labels?: \033[1;33m').lower()
				if len(save_output_A_header_label) <= 0 or save_output_A_header_label.isspace() == True:
					INV_OPT()
					ENC_Output(ENC_BACKUP)
				if save_output_A_header_label == "y":
					if ENC_USED == 'ne' or ENC_USED == 'nd':
						print('#====================================#\n#	     Created by 0xifer	     #\n#====================================#\nInput = ' + text_raw_backup +  '\n\nCode = ' + inputcode_1 + '\n\nOutput = ' + text_raw, file = SO_A_N)
					if ENC_USED == 'ae' or ENC_USED == 'ad':
						print('#====================================#\n#	     Created by 0xifer	     #\n#====================================#\nInput = ' + text_raw_backup +  '\n\nCode #1 = ' + inputcode_1 + '\nCode #2 = ' + inputcode_2 + '\nCode #3 = ' + inputcode_3 + '\nCode #4 = ' + inputcode_4 + '\nCode #5 = ' + inputcode_5 + '\n\nOutput = ' + text_raw, file = SO_A_N)
					if ENC_USED == 'se' or ENC_USED == 'sd':
						print('#====================================#\n#	     Created by 0xifer	     #\n#====================================#\nInput = ' + text_raw_backup +  '\n\nCode #1 = ' + inputcode_1 + '\nCode #2 = ' + inputcode_2 + '\nCode #3 = ' + inputcode_3 + '\nCode #4 = ' + inputcode_4 + '\nCode #5 = ' + inputcode_5 + '\nCode #6 = ' + inputcode_6 + '\nCode #7 = ' + inputcode_7 + '\nCode #8 = ' + inputcode_8 + '\nCode #9 = ' + inputcode_9 + '\nCode #10 = ' + inputcode_10 + '\nCode #11 = ' + inputcode_11 + '\nCode #12 = ' + inputcode_13 + '\nCode #13 = ' + inputcode_14 + '\nCode #14 = ' + inputcode_15 + '\nCode #15 = ' + inputcode_16 + '\nCode #16 = ' + inputcode_17 + '\nCode #17 = ' + inputcode_18 + '\nCode #18 = ' + inputcode_19 + '\nCode #19 = ' + inputcode_20 + '\nCode #20 = ' + inputcode_21 + '\n\nOutput = ' + text_raw, file = SO_A_N)
				if save_output_A_header_label == "n":
					if ENC_USED == 'ne' or ENC_USED == 'nd':
						print('#====================================#\n#	     Created by 0xifer	     #\n#====================================#\n' + text_raw_backup + '\n\n' + inputcode_1 + '\n\n' + text_raw, file = SO_A_N)
					if ENC_USED == 'ae' or ENC_USED == 'ad':
						print('#====================================#\n#	     Created by 0xifer	     #\n#====================================#\n' + text_raw_backup + '\n\n' + inputcode_1 + '\n' + inputcode_2 + '\n' + inputcode_3 + '\n' + inputcode_4 + '\n' + inputcode_5 + '\n\n' + text_raw, file = SO_A_N)
					if ENC_USED == 'se' or ENC_USED == 'sd':
						print('#====================================#\n#	     Created by 0xifer	     #\n#====================================#\n' + text_raw_backup + '\n\n' + inputcode_1 + '\n' + inputcode_2 + '\n' + inputcode_3 + '\n' + inputcode_4 + '\n' + inputcode_5 + '\n' + inputcode_6 + '\n' + inputcode_7 + '\n' + inputcode_8 + '\n' + inputcode_9 + '\n' + inputcode_10 + '\n' + inputcode_11 + '\n' + inputcode_13 + '\n' + inputcode_14 + '\n' + inputcode_15 + '\n' + inputcode_16 + '\n' + inputcode_17 + '\n' + inputcode_18 + '\n' + inputcode_19 + '\n' + inputcode_20 + '\n' + inputcode_21 + '\n\n' + text_raw, file = SO_A_N)
			if save_output_A_header.startswith('n') == True:
				ENC_ADD_LABELS()
				save_output_A_header_label = input('\033[1;36mAdd labels?: \033[1;33m').lower()
				if save_output_A_header_label.startswith('y') == True:
					print('Input = ' + text_raw_backup + '\nLanguage = ' + use_lang + '\nOutput = ' + text_raw, file = SO_A_N) # Print this into the save file
				if save_output_A_header_label.startswith('n') == True:
					print(text_raw_backup + '\n' + use_lang + '\n' + text_raw, file = SO_A_N) # Print this into the save file
				print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
				print('\033[1;31mSuccessfully saved to ' + '\033[1;33m"' + save_output_A_name)
				print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
				time.sleep(2) # Wait
################################################################################################################


################################################################################################################
#                                                     HELP                                                     #
################################################################################################################
def HELP4USER():
	os.system('mode 57,30 && title Help && cls')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	print(' \033[1;33m╔═════════════════════════════════════════════════════╗')
	print(' ║                         \033[1;37mMAIN                        \033[1;33m║')
	print(' ║  \033[1;32mTo start: \033[1;36mChoose a language that you want to use.  \033[1;33m║')
	print(' ║      \033[1;36mTo see all languages available, type "\033[1;33mL\033[1;36m".      \033[1;33m║')
	print(' ║   \033[1;32mNext: \033[1;36mEnter the text that you want to translate   \033[1;33m║')
	print(' ║             \033[1;36minto the language you have chosen       \033[1;33m║')
	print(' ╠═════════════════════════════════════════════════════╣')
	print(' ║                       \033[1;37mCRYPTERS                      \033[1;33m║')
	print(' ║    \033[1;36mThere are 3 different \033[32mEncrypt \033[1;36m/ \033[31mDecrypt \033[1;36mtools    \033[1;33m║')
	print(' ║    Each one has a certain amount of code options    ║')
	print(' ║    \033[1;36mNormal Crypters   \033[1;33m-  \033[1;31m"1" Code   \033[1;33m- \033[1;35m1 ~ 9999       \033[1;0m\033[1;33m║')
	print(' ║    \033[1;36mAdvanced Crypters \033[1;33m-  \033[1;31m"5" Codes  \033[1;33m- \033[1;35m1 ~ 9999       \033[1;0m\033[1;33m║')
	print(' ║    \033[1;36mSuper Crypters    \033[1;33m-  \033[1;31m"20" Codes \033[1;33m- \033[1;35m1 ~ 100,000    \033[1;0m\033[1;33m║')
	print(' ╠═════════════════════════════════════════════════════╣')
	print(' ║             \033[1;37mMULTI-LANGUAGE  TRANSLATORS             \033[1;33m║')
	print(' ║ \033[1;36mIf you are trying to encrypt a text/string with two \033[1;33m║')
	print(' ║  \033[1;36mor more languages at a time, then you can use the  \033[1;33m║')
	print(' ║  \033[1;36mMulti-Language Translator. Enter the language you  \033[1;33m║')
	print(' ║   \033[1;36mwant to use and then the text you want to use.    \033[1;33m║')
	print(' ║  \033[1;36mYou can then enter another language and it will    \033[1;33m║')
	print(' ║  \033[1;36mkeep translating the new text to the new language  \033[1;33m║')
	print(' ╠═════════════════════════════════════════════════════╣')
	print(' ║  \033[1;35mTo see a list of available Commands, enter \033[1;33m"cmd"   \033[1;0m\033[1;33m║')
	print(' ╚═════════════════════════════════════════════════════╝')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;33m')
	getpass('\033[1;33mPress ENTER to continue...')
################################################################################################################


################################################################################################################
#                                                   COMMANDS                                                   #
################################################################################################################
def cmds():
	os.system('mode 57,20 && title All available commands && cls')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;33m')
	print('                ╔════════════════════════╗')
	print(' ╔══════════════╣ \033[1;31mALL AVAILABLE COMMANDS\033[1;33m ╠═════════════╗')
	print(' ║              ╚════════════════════════╝             ║')
	print(' \033[1;33m║ \033[1;0mHELP = \033[1;33m"H"                                          \033[1;33m║')
	print(' \033[1;33m║ \033[1;0mLIST OF POSSIBLE LANGUAGES = \033[1;33m"L"                    \033[1;33m║')
	print(' \033[1;33m║ \033[1;0mALGORITHM VIEWER = \033[1;33m"ALG"                            \033[1;33m║')
	print(' \033[1;33m║ \033[1;0mMULTI-LANGUAGE TRANSLATOR = \033[1;33m"MT"                    \033[1;33m║')
	print(' \033[1;33m║ \033[1;0mREVERSE MULTI-LANGUAGE TRANSLATOR = \033[1;33m"RMT"           \033[1;33m║')
	print(' \033[1;33m║ \033[1;0mNORMAL ENCRYPTER = \033[1;33m"E"                              \033[1;33m║')
	print(' \033[1;33m║ \033[1;0mNORMAL DECRYPTER = \033[1;33m"D"                              \033[1;33m║')
	print(' \033[1;33m║ \033[1;0mADVANCED ENCRYPTER = \033[1;33m"AE"                           \033[1;33m║')
	print(' \033[1;33m║ \033[1;0mADVANCED DECRYPTER = \033[1;33m"AD"                           \033[1;33m║')
	print(' \033[1;33m║ \033[1;0mSUPER ENCRYPTER = \033[1;33m"SE"                              \033[1;33m║')
	print(' \033[1;33m║ \033[1;0mSUPER DECRYPTER = \033[1;33m"SD"                              \033[1;33m║')
	print(' \033[1;33m║ \033[1;0mSHOW LETTERS OF A ALPHABET = \033[1;33m"S"                    \033[1;33m║')
	print(' \033[1;33m║ \033[1;0mCREATE YOUR OWN LANGUAGE = \033[1;33m"C"                      \033[1;33m║')
	print(' \033[1;33m║ \033[1;0mREVERSE/DECRYPT WITH GIVEN ALPHABET = \033[1;33m"R"           \033[1;33m║')
	print(' \033[1;33m╚═════════════════════════════════════════════════════╝')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	getpass('\033[1;33mPress ENTER to continue...')
################################################################################################################


################################################################################################################
#                                                 LANGUAGE LIST                                                #
################################################################################################################
def list_langs():
	os.system('mode 57,27 && title All available alphabets/languages && cls')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;33m')
	print('                  ╔═════════════════════╗')
	print(' ╔════════════════╣\033[1;31m  List of Languages  \033[1;33m╠══════════════╗')
	print(' ║                ╚═════════════════════╝              ║')
	print(' \033[1;33m║\033[1;0m BACKWARDS ALPHABET = \033[1;33m"BW"                           \033[1;33m║')
	print(' \033[1;33m║\033[1;0m RYA LANGUAGE= \033[1;33m"RYA"                                 \033[1;33m║')
	print(' \033[1;33m║\033[1;0m LAZY LANGUAGE = \033[1;33m"LAZY"                              \033[1;33m║')
	print(' \033[1;33m║\033[1;0m 0X\'s LANGUAGE = \033[1;33m"0X"                                \033[1;33m║')
	print(' \033[1;33m║\033[1;0m 0X\'s LANGUAGE-QWERTY EDITION = \033[1;33m"0XQ"                \033[1;33m║')
	print(' \033[1;33m║\033[1;0m CRAZY LANGUAGE = \033[1;33m"CRAZY"                            \033[1;33m║')
	print(' \033[1;33m║\033[1;0m CRAZY LANGUAGE #2 = \033[1;33m"CRAZY2"                        \033[1;33m║')
	print(' \033[1;33m║\033[1;0m 1337 5P34K = \033[1;33m"LEET"                                 \033[1;33m║')
	print(' \033[1;33m║\033[1;0m BINARY CODE = \033[1;33m"BINARY"                              \033[1;33m║')
	print(' \033[1;33m║\033[1;0m SHIFTED 3 TO THE RIGHT = \033[1;33m"3R"                       \033[1;33m║')
	print(' \033[1;33m║\033[1;0m SHIFTED 3 TO THE LEFT = \033[1;33m"3L"                        \033[1;33m║')
	print(' \033[1;33m║\033[1;0m SHIFTED 2 TO THE RIGHT = \033[1;33m"2R"                       \033[1;33m║')
	print(' \033[1;33m║\033[1;0m SHIFTED 2 TO THE LEFT = \033[1;33m"2L"                        \033[1;33m║')
	print(' \033[1;33m║\033[1;0m SHIFTED 1 TO THE RIGHT = \033[1;33m"1R"                       \033[1;33m║')
	print(' \033[1;33m║\033[1;0m SHIFTED 1 TO THE LEFT = \033[1;33m"1L"                        \033[1;33m║')
	print(' \033[1;33m║\033[1;0m VOWEL REPLACER = \033[1;33m"VR"                               \033[1;33m║')
	print(' \033[1;33m║\033[1;0m UPPERCASE = \033[1;33m"UC"                                    \033[1;33m║')
	print(' \033[1;33m║\033[1;0m LOWERCASE = \033[1;33m"LC"                                    \033[1;33m║')
	print(' \033[1;33m║                \033[1;31m╔══════════════════════╗             \033[1;33m║')
	print(' \033[1;33m╚════════════════\033[1;31m║ ENTER \033[1;33m"B"\033[1;31m TO GO BACK ║\033[1;33m═════════════╝')
	print('                  \033[1;31m╚══════════════════════╝')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;33m')
	getpass('\033[1;33mPress ENTER to continue...')
################################################################################################################


################################################################################################################
#                                                SUPER ENCRYPTER                                               #
################################################################################################################
def S_ENCRYPT():
	global SE_Seperator, inputcode_1, inputcode_2, inputcode_3, inputcode_4, inputcode_5, inputcode_6, inputcode_7, inputcode_8, inputcode_9, inputcode_10, inputcode_11, inputcode_13, inputcode_14, inputcode_15, inputcode_16, inputcode_17, inputcode_18, inputcode_19, inputcode_20, inputcode_21
	os.system('mode 57,21 && title Super Encrypter && cls')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;33m')
	print('                  ╔═══════════════════╗')
	print('     ╔════════════╣\033[1;31m  Super Encrypter  \033[1;33m╠════════════╗')
	print('     ║            ╚═══════════════════╝            ║')
	print('     ║    \033[1;33m1. \033[1;36mEnter all 20 codes to secure with     \033[1;33m║')
	print('     ║        \033[1;33m2. \033[1;36mEnter the text to encrypt         \033[1;33m║')
	print('     ║     \033[1;35m-Enter \033[1;33m"auto"\033[1;35m to change all codes-      \033[1;33m║')
	print('     ║             \033[1;31mENTER \033[1;33m"B"\033[1;31m TO GO BACK            \033[1;33m║')
	print('     ║        ╔════════════════════════════╗       ║')
	print('     ╚════════╣ \033[1;31m# of possible combinations\033[1;33m ╠═══════╝\033[1;33m')
	print('              ║          \033[1;36m1 Googol          \033[1;33m║')
	print('              ╚════════════════════════════╝')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	SE_Seperator = input('\033[1;36mSeperator \033[1;35m[\033[1;31mLETTERS \033[1;36m+ \033[1;31mSYMBOLS ONLY\033[1;35m]\033[1;36m: \033[1;33m')
	if len(SE_Seperator) <= 0:
		S_ENCRYPT()
	CANT_PASS = '0123456789'
	for a in CANT_PASS:
		for b in SE_Seperator:
			if a == b:
				INV_OPT()
				S_ENCRYPT()
	inputcode_eval_1 = input('\033[1;36mFirst code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_1)
	inputcode_1 = int(inputcode_eval_1)
	inputcode_eval_2 = input('\033[1;36mSecond code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_2)
	inputcode_2 = int(inputcode_eval_2)
	inputcode_eval_3 = input('\033[1;36mThird code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_3)
	inputcode_3 = int(inputcode_eval_3)
	inputcode_eval_4 = input('\033[1;36mFourth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_4)
	inputcode_4 = int(inputcode_eval_4)
	inputcode_eval_5 = input('\033[1;36mFifth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_5)
	inputcode_5 = int(inputcode_eval_5)
	inputcode_eval_6 = input('\033[1;36mSixth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_6)
	inputcode_6 = int(inputcode_eval_6)
	inputcode_eval_7 = input('\033[1;36mSeventh code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_7)
	inputcode_7 = int(inputcode_eval_7)
	inputcode_eval_8 = input('\033[1;36mEighth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_8)
	inputcode_8 = int(inputcode_eval_8)
	inputcode_eval_9 = input('\033[1;36mNinth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_9)
	inputcode_9 = int(inputcode_eval_9)
	inputcode_eval_10 = input('\033[1;36mTenth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_10)
	inputcode_10 = int(inputcode_eval_10)
	inputcode_eval_11 = input('\033[1;36mEleventh code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_11)
	inputcode_11 = int(inputcode_eval_11)
	inputcode_eval_13 = input('\033[1;36mTwelfth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_13)
	inputcode_13 = int(inputcode_eval_13)
	inputcode_eval_14 = input('\033[1;36mThirteenth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_14)
	inputcode_14 = int(inputcode_eval_14)
	inputcode_eval_15 = input('\033[1;36mFourteenth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_15)
	inputcode_15 = int(inputcode_eval_15)
	inputcode_eval_16 = input('\033[1;36mFifteenth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_16)
	inputcode_16 = int(inputcode_eval_16)
	inputcode_eval_17 = input('\033[1;36mSixteenth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_17)
	inputcode_17 = int(inputcode_eval_17)
	inputcode_eval_18 = input('\033[1;36mSeventeenth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_18)
	inputcode_18 = int(inputcode_eval_18)
	inputcode_eval_19 = input('\033[1;36mEighteenth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_19)
	inputcode_19 = int(inputcode_eval_19)
	inputcode_eval_20 = input('\033[1;36mNineteenth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_20)
	inputcode_20 = int(inputcode_eval_20)
	inputcode_eval_21 = input('\033[1;36mTwentieth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SE_CHECKER(inputcode_eval_21)
	inputcode_21 = int(inputcode_eval_21)

	SE_ENDING()

def SE_ENDING():
	T2E()
	S_ENCRYPT_NUMBERS()
	ENC_Output('se')
	S_ENCRYPT()

def SE_CHECKER(input_1):
	global inputcode_1, inputcode_2, inputcode_3, inputcode_4, inputcode_5, inputcode_6, inputcode_7, inputcode_8, inputcode_9, inputcode_10, inputcode_11, inputcode_13, inputcode_14, inputcode_15, inputcode_16, inputcode_17, inputcode_18, inputcode_19, inputcode_20, inputcode_21
	if input_1 == 'auto':
		AutoCode = input('\033[1;36mEnter the number for all codes: \033[1;33m')
		SE_STRINGCHECK(AutoCode)
		SE_CODECHECK(AutoCode)
		inputcode_1 = inputcode_2 = inputcode_3 = inputcode_4 = inputcode_5 = inputcode_6 = inputcode_7 = inputcode_8 = inputcode_9 = inputcode_10 = inputcode_11 = inputcode_13 = inputcode_14 = inputcode_15 = inputcode_16 = inputcode_17 = inputcode_18 = inputcode_19 = inputcode_20 = inputcode_21 = int(AutoCode)
		SE_ENDING()
	SE_STRINGCHECK(input_1)
	SE_CODECHECK(input_1)

def SE_STRINGCHECK(inputcode):
	if len(inputcode) <= 0 or inputcode.isspace() == True:
		INV_OPT()
		S_ENCRYPT()
	if inputcode == 'b':
		Main()
	CANT_PASS = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+|{}:"<>?`-=\\[];\',./' # List of all the text that would be considered 'not allowed'
	for a in CANT_PASS:
		for b in inputcode:
			if a == b:
				INV_OPT()
				S_ENCRYPT()

def SE_CODECHECK(inputcode):
	inputcode = int(inputcode)
	if inputcode <= 0 or inputcode > 100000:
		INV_OPT()
		S_ENCRYPT()
################################################################################################################


def S_ENCRYPT_NUMBERS():
	global text_raw
	inputcode_22 = inputcode_1 + inputcode_2 * inputcode_3 + inputcode_4 - inputcode_5 - inputcode_6 + inputcode_7 * inputcode_8 + inputcode_9 - inputcode_10 - inputcode_11 + inputcode_13 * inputcode_14 + inputcode_15 - inputcode_16 - inputcode_17 + inputcode_18 * inputcode_19 + inputcode_20 - inputcode_21
	E_S_1 = str(7 * inputcode_22 * 2055) + SE_Seperator
	E_S_a = str(17 * inputcode_22 * 2055) + SE_Seperator
	E_S_b = str(27 * inputcode_22 * 2055) + SE_Seperator
	E_S_c = str(37 * inputcode_22 * 2055) + SE_Seperator
	E_S_d = str(47 * inputcode_22 * 2055) + SE_Seperator
	E_S_e = str(57 * inputcode_22 * 2055) + SE_Seperator
	E_S_f = str(67 * inputcode_22 * 2055) + SE_Seperator
	E_S_g = str(77 * inputcode_22 * 2055) + SE_Seperator
	E_S_h = str(87 * inputcode_22 * 2055) + SE_Seperator
	E_S_i = str(97 * inputcode_22 * 2055) + SE_Seperator
	E_S_j = str(107 * inputcode_22 * 2055) + SE_Seperator
	E_S_k = str(117 * inputcode_22 * 2055) + SE_Seperator
	E_S_l = str(137 * inputcode_22 * 2055) + SE_Seperator
	E_S_m = str(147 * inputcode_22 * 2055) + SE_Seperator
	E_S_n = str(157 * inputcode_22 * 2055) + SE_Seperator
	E_S_o = str(167 * inputcode_22 * 2055) + SE_Seperator
	E_S_p = str(177 * inputcode_22 * 2055) + SE_Seperator
	E_S_q = str(187 * inputcode_22 * 2055) + SE_Seperator
	E_S_r = str(197 * inputcode_22 * 2055) + SE_Seperator
	E_S_s = str(207 * inputcode_22 * 2055) + SE_Seperator
	E_S_t = str(217 * inputcode_22 * 2055) + SE_Seperator
	E_S_u = str(227 * inputcode_22 * 2055) + SE_Seperator
	E_S_v = str(237 * inputcode_22 * 2055) + SE_Seperator
	E_S_w = str(247 * inputcode_22 * 2055) + SE_Seperator
	E_S_x = str(257 * inputcode_22 * 2055) + SE_Seperator
	E_S_y = str(267 * inputcode_22 * 2055) + SE_Seperator
	E_S_z = str(277 * inputcode_22 * 2055) + SE_Seperator
	E_S_A = str(287 * inputcode_22 * 2055) + SE_Seperator
	E_S_B = str(297 * inputcode_22 * 2055) + SE_Seperator
	E_S_C = str(307 * inputcode_22 * 2055) + SE_Seperator
	E_S_D = str(317 * inputcode_22 * 2055) + SE_Seperator
	E_S_E = str(327 * inputcode_22 * 2055) + SE_Seperator
	E_S_F = str(337 * inputcode_22 * 2055) + SE_Seperator
	E_S_G = str(347 * inputcode_22 * 2055) + SE_Seperator
	E_S_H = str(357 * inputcode_22 * 2055) + SE_Seperator
	E_S_I = str(367 * inputcode_22 * 2055) + SE_Seperator
	E_S_J = str(377 * inputcode_22 * 2055) + SE_Seperator
	E_S_K = str(387 * inputcode_22 * 2055) + SE_Seperator
	E_S_L = str(397 * inputcode_22 * 2055) + SE_Seperator
	E_S_M = str(407 * inputcode_22 * 2055) + SE_Seperator
	E_S_N = str(417 * inputcode_22 * 2055) + SE_Seperator
	E_S_O = str(427 * inputcode_22 * 2055) + SE_Seperator
	E_S_P = str(437 * inputcode_22 * 2055) + SE_Seperator
	E_S_Q = str(447 * inputcode_22 * 2055) + SE_Seperator
	E_S_R = str(457 * inputcode_22 * 2055) + SE_Seperator
	E_S_S = str(467 * inputcode_22 * 2055) + SE_Seperator
	E_S_T = str(477 * inputcode_22 * 2055) + SE_Seperator
	E_S_U = str(487 * inputcode_22 * 2055) + SE_Seperator
	E_S_V = str(497 * inputcode_22 * 2055) + SE_Seperator
	E_S_W = str(507 * inputcode_22 * 2055) + SE_Seperator
	E_S_X = str(517 * inputcode_22 * 2055) + SE_Seperator
	E_S_Y = str(527 * inputcode_22 * 2055) + SE_Seperator
	E_S_Z = str(537 * inputcode_22 * 2055) + SE_Seperator
	text_raw = text_raw.replace(' ',E_S_1)
	text_raw = text_raw.replace('a',E_S_a)
	text_raw = text_raw.replace('b',E_S_b)
	text_raw = text_raw.replace('c',E_S_c)
	text_raw = text_raw.replace('d',E_S_d)
	text_raw = text_raw.replace('e',E_S_e)
	text_raw = text_raw.replace('f',E_S_f)
	text_raw = text_raw.replace('g',E_S_g)
	text_raw = text_raw.replace('h',E_S_h)
	text_raw = text_raw.replace('i',E_S_i)
	text_raw = text_raw.replace('j',E_S_j)
	text_raw = text_raw.replace('k',E_S_k)
	text_raw = text_raw.replace('l',E_S_l)
	text_raw = text_raw.replace('m',E_S_m)
	text_raw = text_raw.replace('n',E_S_n)
	text_raw = text_raw.replace('o',E_S_o)
	text_raw = text_raw.replace('p',E_S_p)
	text_raw = text_raw.replace('q',E_S_q)
	text_raw = text_raw.replace('r',E_S_r)
	text_raw = text_raw.replace('s',E_S_s)
	text_raw = text_raw.replace('t',E_S_t)
	text_raw = text_raw.replace('u',E_S_u)
	text_raw = text_raw.replace('v',E_S_v)
	text_raw = text_raw.replace('w',E_S_w)
	text_raw = text_raw.replace('x',E_S_x)
	text_raw = text_raw.replace('y',E_S_y)
	text_raw = text_raw.replace('z',E_S_z)
	text_raw = text_raw.replace('A',E_S_A)
	text_raw = text_raw.replace('B',E_S_B)
	text_raw = text_raw.replace('C',E_S_C)
	text_raw = text_raw.replace('D',E_S_D)
	text_raw = text_raw.replace('E',E_S_E)
	text_raw = text_raw.replace('F',E_S_F)
	text_raw = text_raw.replace('G',E_S_G)
	text_raw = text_raw.replace('H',E_S_H)
	text_raw = text_raw.replace('I',E_S_I)
	text_raw = text_raw.replace('J',E_S_J)
	text_raw = text_raw.replace('K',E_S_K)
	text_raw = text_raw.replace('L',E_S_L)
	text_raw = text_raw.replace('M',E_S_M)
	text_raw = text_raw.replace('N',E_S_N)
	text_raw = text_raw.replace('O',E_S_O)
	text_raw = text_raw.replace('P',E_S_P)
	text_raw = text_raw.replace('Q',E_S_Q)
	text_raw = text_raw.replace('R',E_S_R)
	text_raw = text_raw.replace('S',E_S_S)
	text_raw = text_raw.replace('T',E_S_T)
	text_raw = text_raw.replace('U',E_S_U)
	text_raw = text_raw.replace('V',E_S_V)
	text_raw = text_raw.replace('W',E_S_W)
	text_raw = text_raw.replace('X',E_S_X)
	text_raw = text_raw.replace('Y',E_S_Y)
	text_raw = text_raw.replace('Z',E_S_Z)
################################################################################################################


################################################################################################################
#                                              ADVANCED ENCRYPTER                                              #
################################################################################################################
def A_ENCRYPT():
	global AE_Seperator, inputcode_1, inputcode_2, inputcode_3, inputcode_4, inputcode_5
	os.system('mode 57,20 && title Advanced Encrypter && cls')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;33m')
	print('                 ╔════════════════════╗')
	print('     ╔═══════════╣\033[1;36m Advanced \033[1;31mEncrypter \033[1;33m╠═══════════╗')
	print('     ║           ╚════════════════════╝           ║')
	print('     ║ \033[1;33m1. \033[1;36mEnter 5 codes to secure your text with  \033[1;33m║')
	print('     ║        \033[1;33m2. \033[1;36mEnter the text to encrypt        \033[1;33m║')
	print('     ║     \033[1;35m-Enter \033[1;33m"auto"\033[1;35m to change all codes-     \033[1;33m║')
	print('     ║            \033[1;31mENTER \033[1;33m"B"\033[1;31m TO GO BACK            \033[1;33m║')
	print('     ║       ╔════════════════════════════╗       ║')
	print('     ╚═══════╣ \033[1;31m# of possible combinations\033[1;33m ╠═══════╝\033[1;33m')
	print('             ║ \033[1;36m99,950,010,000,000,000,000 \033[1;33m║')
	print('             ╚════════════════════════════╝')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	AE_Seperator = input('\033[1;36mSeperator \033[1;35m[\033[1;31mLETTERS \033[1;36m+ \033[1;31mSYMBOLS ONLY\033[1;35m]\033[1;36m: \033[1;33m')
	if len(AE_Seperator) <= 0:
		A_ENCRYPT()
	CANT_PASS = '0123456789'
	for a in CANT_PASS:
		for b in AE_Seperator:
			if a == b:
				INV_OPT()
				A_ENCRYPT()
	inputcode_eval_1 = input('\033[1;36mFirst code \033[1;35m1 ~ 9,999\033[1;36m: \033[1;33m').lower()
	AE_CHECKER(inputcode_eval_1)
	inputcode_1 = int(inputcode_eval_1)
	inputcode_eval_2 = input('\033[1;36mSecond code \033[1;35m1 ~ 9,999\033[1;36m: \033[1;33m').lower()
	AE_CHECKER(inputcode_eval_2)
	inputcode_2 = int(inputcode_eval_2)
	inputcode_eval_3 = input('\033[1;36mThird code \033[1;35m1 ~ 9,999\033[1;36m: \033[1;33m').lower()
	AE_CHECKER(inputcode_eval_3)
	inputcode_3 = int(inputcode_eval_3)
	inputcode_eval_4 = input('\033[1;36mFourth code \033[1;35m1 ~ 9,999\033[1;36m: \033[1;33m').lower()
	AE_CHECKER(inputcode_eval_4)
	inputcode_4 = int(inputcode_eval_4)
	inputcode_eval_5 = input('\033[1;36mFifth code \033[1;35m1 ~ 9,999\033[1;36m: \033[1;33m').lower()
	AE_CHECKER(inputcode_eval_5)
	inputcode_5 = int(inputcode_eval_5)

	AE_ENDING()

def AE_ENDING():
	T2E()
	A_ENCRYPT_NUMBERS()
	ENC_Output('ae')
	A_ENCRYPT()

def AE_CHECKER(input_1):
	global inputcode_1, inputcode_2, inputcode_3, inputcode_4, inputcode_5
	if input_1 == 'auto':
		AutoCode = input('\033[1;36mEnter the number for all codes: \033[1;33m')
		AE_STRINGCHECK(AutoCode)
		AE_CODECHECK(AutoCode)
		inputcode_1 = inputcode_2 = inputcode_3 = inputcode_4 = inputcode_5 = int(AutoCode)
		AE_ENDING()
	AE_STRINGCHECK(input_1)
	AE_CODECHECK(input_1)

def AE_STRINGCHECK(inputcode):
	if len(inputcode) <= 0 or inputcode.isspace() == True:
		A_ENCRYPT()
	if inputcode == 'b':
		Main()
	CANT_PASS = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+|{}:"<>?`-=\\[];\',./' # List of all the text that would be considered 'not allowed'
	for a in CANT_PASS:
		for b in inputcode:
			if a == b:
				INV_OPT()
				A_ENCRYPT()

def AE_CODECHECK(inputcode):
	inputcode = int(inputcode)
	if inputcode <= 0 or inputcode > 9999:
		INV_OPT()
		A_ENCRYPT()
################################################################################################################


def A_ENCRYPT_NUMBERS():
	global text_raw
	inputcode_6 = inputcode_1 + inputcode_2 * inputcode_3 + inputcode_4 * inputcode_5
	E_A_1 = str(7 * inputcode_6 * 2055) + AE_Seperator
	E_A_a = str(17 * inputcode_6 * 2055) + AE_Seperator
	E_A_b = str(27 * inputcode_6 * 2055) + AE_Seperator
	E_A_c = str(37 * inputcode_6 * 2055) + AE_Seperator
	E_A_d = str(47 * inputcode_6 * 2055) + AE_Seperator
	E_A_e = str(57 * inputcode_6 * 2055) + AE_Seperator
	E_A_f = str(67 * inputcode_6 * 2055) + AE_Seperator
	E_A_g = str(77 * inputcode_6 * 2055) + AE_Seperator
	E_A_h = str(87 * inputcode_6 * 2055) + AE_Seperator
	E_A_i = str(97 * inputcode_6 * 2055) + AE_Seperator
	E_A_j = str(107 * inputcode_6 * 2055) + AE_Seperator
	E_A_k = str(117 * inputcode_6 * 2055) + AE_Seperator
	E_A_l = str(137 * inputcode_6 * 2055) + AE_Seperator
	E_A_m = str(147 * inputcode_6 * 2055) + AE_Seperator
	E_A_n = str(157 * inputcode_6 * 2055) + AE_Seperator
	E_A_o = str(167 * inputcode_6 * 2055) + AE_Seperator
	E_A_p = str(177 * inputcode_6 * 2055) + AE_Seperator
	E_A_q = str(187 * inputcode_6 * 2055) + AE_Seperator
	E_A_r = str(197 * inputcode_6 * 2055) + AE_Seperator
	E_A_s = str(207 * inputcode_6 * 2055) + AE_Seperator
	E_A_t = str(217 * inputcode_6 * 2055) + AE_Seperator
	E_A_u = str(227 * inputcode_6 * 2055) + AE_Seperator
	E_A_v = str(237 * inputcode_6 * 2055) + AE_Seperator
	E_A_w = str(247 * inputcode_6 * 2055) + AE_Seperator
	E_A_x = str(257 * inputcode_6 * 2055) + AE_Seperator
	E_A_y = str(267 * inputcode_6 * 2055) + AE_Seperator
	E_A_z = str(277 * inputcode_6 * 2055) + AE_Seperator
	E_A_A = str(287 * inputcode_6 * 2055) + AE_Seperator
	E_A_B = str(297 * inputcode_6 * 2055) + AE_Seperator
	E_A_C = str(307 * inputcode_6 * 2055) + AE_Seperator
	E_A_D = str(317 * inputcode_6 * 2055) + AE_Seperator
	E_A_E = str(327 * inputcode_6 * 2055) + AE_Seperator
	E_A_F = str(337 * inputcode_6 * 2055) + AE_Seperator
	E_A_G = str(347 * inputcode_6 * 2055) + AE_Seperator
	E_A_H = str(357 * inputcode_6 * 2055) + AE_Seperator
	E_A_I = str(367 * inputcode_6 * 2055) + AE_Seperator
	E_A_J = str(377 * inputcode_6 * 2055) + AE_Seperator
	E_A_K = str(387 * inputcode_6 * 2055) + AE_Seperator
	E_A_L = str(397 * inputcode_6 * 2055) + AE_Seperator
	E_A_M = str(407 * inputcode_6 * 2055) + AE_Seperator
	E_A_N = str(417 * inputcode_6 * 2055) + AE_Seperator
	E_A_O = str(427 * inputcode_6 * 2055) + AE_Seperator
	E_A_P = str(437 * inputcode_6 * 2055) + AE_Seperator
	E_A_Q = str(447 * inputcode_6 * 2055) + AE_Seperator
	E_A_R = str(457 * inputcode_6 * 2055) + AE_Seperator
	E_A_S = str(467 * inputcode_6 * 2055) + AE_Seperator
	E_A_T = str(477 * inputcode_6 * 2055) + AE_Seperator
	E_A_U = str(487 * inputcode_6 * 2055) + AE_Seperator
	E_A_V = str(497 * inputcode_6 * 2055) + AE_Seperator
	E_A_W = str(507 * inputcode_6 * 2055) + AE_Seperator
	E_A_X = str(517 * inputcode_6 * 2055) + AE_Seperator
	E_A_Y = str(527 * inputcode_6 * 2055) + AE_Seperator
	E_A_Z = str(537 * inputcode_6 * 2055) + AE_Seperator
	text_raw = text_raw.replace(' ',E_A_1)
	text_raw = text_raw.replace('a',E_A_a)
	text_raw = text_raw.replace('b',E_A_b)
	text_raw = text_raw.replace('c',E_A_c)
	text_raw = text_raw.replace('d',E_A_d)
	text_raw = text_raw.replace('e',E_A_e)
	text_raw = text_raw.replace('f',E_A_f)
	text_raw = text_raw.replace('g',E_A_g)
	text_raw = text_raw.replace('h',E_A_h)
	text_raw = text_raw.replace('i',E_A_i)
	text_raw = text_raw.replace('j',E_A_j)
	text_raw = text_raw.replace('k',E_A_k)
	text_raw = text_raw.replace('l',E_A_l)
	text_raw = text_raw.replace('m',E_A_m)
	text_raw = text_raw.replace('n',E_A_n)
	text_raw = text_raw.replace('o',E_A_o)
	text_raw = text_raw.replace('p',E_A_p)
	text_raw = text_raw.replace('q',E_A_q)
	text_raw = text_raw.replace('r',E_A_r)
	text_raw = text_raw.replace('s',E_A_s)
	text_raw = text_raw.replace('t',E_A_t)
	text_raw = text_raw.replace('u',E_A_u)
	text_raw = text_raw.replace('v',E_A_v)
	text_raw = text_raw.replace('w',E_A_w)
	text_raw = text_raw.replace('x',E_A_x)
	text_raw = text_raw.replace('y',E_A_y)
	text_raw = text_raw.replace('z',E_A_z)
	text_raw = text_raw.replace('A',E_A_A)
	text_raw = text_raw.replace('B',E_A_B)
	text_raw = text_raw.replace('C',E_A_C)
	text_raw = text_raw.replace('D',E_A_D)
	text_raw = text_raw.replace('E',E_A_E)
	text_raw = text_raw.replace('F',E_A_F)
	text_raw = text_raw.replace('G',E_A_G)
	text_raw = text_raw.replace('H',E_A_H)
	text_raw = text_raw.replace('I',E_A_I)
	text_raw = text_raw.replace('J',E_A_J)
	text_raw = text_raw.replace('K',E_A_K)
	text_raw = text_raw.replace('L',E_A_L)
	text_raw = text_raw.replace('M',E_A_M)
	text_raw = text_raw.replace('N',E_A_N)
	text_raw = text_raw.replace('O',E_A_O)
	text_raw = text_raw.replace('P',E_A_P)
	text_raw = text_raw.replace('Q',E_A_Q)
	text_raw = text_raw.replace('R',E_A_R)
	text_raw = text_raw.replace('S',E_A_S)
	text_raw = text_raw.replace('T',E_A_T)
	text_raw = text_raw.replace('U',E_A_U)
	text_raw = text_raw.replace('V',E_A_V)
	text_raw = text_raw.replace('W',E_A_W)
	text_raw = text_raw.replace('X',E_A_X)
	text_raw = text_raw.replace('Y',E_A_Y)
	text_raw = text_raw.replace('Z',E_A_Z)
################################################################################################################


################################################################################################################
#                                               NORMAL ENCRYPTER                                               #
################################################################################################################
def N_ENCRYPT():
	global NE_Seperator, inputcode_1
	os.system('mode 57,20 && title Normal Encrypter && cls')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;33m')
	print('                 ╔════════════════════╗')
	print('     ╔═══════════╣\033[1;36m  Normal \033[1;31mEncrypter  \033[1;33m╠═══════════╗')
	print('     ║           ╚════════════════════╝           ║')
	print('     ║ \033[1;33m1. \033[1;36mEnter a # code to secure your text with \033[1;33m║')
	print('     ║    \033[1;33m2. \033[1;36mEnter the text you want to encrypt   \033[1;33m║')
	print('     ║           \033[1;31m-ENTER \033[1;33m"B"\033[1;31m TO GO BACK-           \033[1;33m║')
	print('     ║       ╔════════════════════════════╗       ║')
	print('     ╚═══════╣ \033[1;31m# of possible combinations\033[1;33m ╠═══════╝\033[1;33m')
	print('             ║            \033[1;36m9,999           \033[1;33m║')
	print('             ╚════════════════════════════╝')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	NE_Seperator = input('\033[1;36mSeperator \033[1;35m[\033[1;31mLETTERS \033[1;36m+ \033[1;31mSYMBOLS ONLY\033[1;35m]\033[1;36m: \033[1;33m')
	if len(NE_Seperator) <= 0:
		N_ENCRYPT()
	CANT_PASS = '0123456789'
	for a in CANT_PASS:
		for b in NE_Seperator:
			if a == b:
				INV_OPT()
				N_ENCRYPT()
	inputcode_eval = input('\033[1;36mCode \033[1;35m1 ~ 9,999\033[1;36m: \033[1;33m').lower()
	if len(inputcode_eval) <= 0 or inputcode_eval.isspace() == True:
		N_ENCRYPT()
	if inputcode_eval == 'b':
		Main()
	CANT_PASS = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+|{}:"<>?`-=\\[];\',./' # List of all the text that would be considered 'not allowed'
	for a in CANT_PASS:
		for b in inputcode_eval:
			if a == b:
				INV_OPT()
				N_ENCRYPT()
	inputcode_1 = int(inputcode_eval)
	if inputcode_1 <= 0 or inputcode_1 > 9999:
		INV_OPT()
		N_ENCRYPT()
	T2E()
	N_ENCRYPT_NUMBERS()
	ENC_Output('ne')
	N_ENCRYPT()
################################################################################################################


def N_ENCRYPT_NUMBERS():
	global text_raw, inputcode_1
	E_N_1 = str(7 * inputcode_1 * 2055) + NE_Seperator
	E_N_a = str(17 * inputcode_1 * 2055) + NE_Seperator
	E_N_b = str(27 * inputcode_1 * 2055) + NE_Seperator
	E_N_c = str(37 * inputcode_1 * 2055) + NE_Seperator
	E_N_d = str(47 * inputcode_1 * 2055) + NE_Seperator
	E_N_e = str(57 * inputcode_1 * 2055) + NE_Seperator
	E_N_f = str(67 * inputcode_1 * 2055) + NE_Seperator
	E_N_g = str(77 * inputcode_1 * 2055) + NE_Seperator
	E_N_h = str(87 * inputcode_1 * 2055) + NE_Seperator
	E_N_i = str(97 * inputcode_1 * 2055) + NE_Seperator
	E_N_j = str(107 * inputcode_1 * 2055) + NE_Seperator
	E_N_k = str(117 * inputcode_1 * 2055) + NE_Seperator
	E_N_l = str(137 * inputcode_1 * 2055) + NE_Seperator
	E_N_m = str(147 * inputcode_1 * 2055) + NE_Seperator
	E_N_n = str(157 * inputcode_1 * 2055) + NE_Seperator
	E_N_o = str(167 * inputcode_1 * 2055) + NE_Seperator
	E_N_p = str(177 * inputcode_1 * 2055) + NE_Seperator
	E_N_q = str(187 * inputcode_1 * 2055) + NE_Seperator
	E_N_r = str(197 * inputcode_1 * 2055) + NE_Seperator
	E_N_s = str(207 * inputcode_1 * 2055) + NE_Seperator
	E_N_t = str(217 * inputcode_1 * 2055) + NE_Seperator
	E_N_u = str(227 * inputcode_1 * 2055) + NE_Seperator
	E_N_v = str(237 * inputcode_1 * 2055) + NE_Seperator
	E_N_w = str(247 * inputcode_1 * 2055) + NE_Seperator
	E_N_x = str(257 * inputcode_1 * 2055) + NE_Seperator
	E_N_y = str(267 * inputcode_1 * 2055) + NE_Seperator
	E_N_z = str(277 * inputcode_1 * 2055) + NE_Seperator
	E_N_A = str(287 * inputcode_1 * 2055) + NE_Seperator
	E_N_B = str(297 * inputcode_1 * 2055) + NE_Seperator
	E_N_C = str(307 * inputcode_1 * 2055) + NE_Seperator
	E_N_D = str(317 * inputcode_1 * 2055) + NE_Seperator
	E_N_E = str(327 * inputcode_1 * 2055) + NE_Seperator
	E_N_F = str(337 * inputcode_1 * 2055) + NE_Seperator
	E_N_G = str(347 * inputcode_1 * 2055) + NE_Seperator
	E_N_H = str(357 * inputcode_1 * 2055) + NE_Seperator
	E_N_I = str(367 * inputcode_1 * 2055) + NE_Seperator
	E_N_J = str(377 * inputcode_1 * 2055) + NE_Seperator
	E_N_K = str(387 * inputcode_1 * 2055) + NE_Seperator
	E_N_L = str(397 * inputcode_1 * 2055) + NE_Seperator
	E_N_M = str(407 * inputcode_1 * 2055) + NE_Seperator
	E_N_N = str(417 * inputcode_1 * 2055) + NE_Seperator
	E_N_O = str(427 * inputcode_1 * 2055) + NE_Seperator
	E_N_P = str(437 * inputcode_1 * 2055) + NE_Seperator
	E_N_Q = str(447 * inputcode_1 * 2055) + NE_Seperator
	E_N_R = str(457 * inputcode_1 * 2055) + NE_Seperator
	E_N_S = str(467 * inputcode_1 * 2055) + NE_Seperator
	E_N_T = str(477 * inputcode_1 * 2055) + NE_Seperator
	E_N_U = str(487 * inputcode_1 * 2055) + NE_Seperator
	E_N_V = str(497 * inputcode_1 * 2055) + NE_Seperator
	E_N_W = str(507 * inputcode_1 * 2055) + NE_Seperator
	E_N_X = str(517 * inputcode_1 * 2055) + NE_Seperator
	E_N_Y = str(527 * inputcode_1 * 2055) + NE_Seperator
	E_N_Z = str(537 * inputcode_1 * 2055) + NE_Seperator
	text_raw = text_raw.replace(' ',E_N_1)
	text_raw = text_raw.replace('a',E_N_a)
	text_raw = text_raw.replace('b',E_N_b)
	text_raw = text_raw.replace('c',E_N_c)
	text_raw = text_raw.replace('d',E_N_d)
	text_raw = text_raw.replace('e',E_N_e)
	text_raw = text_raw.replace('f',E_N_f)
	text_raw = text_raw.replace('g',E_N_g)
	text_raw = text_raw.replace('h',E_N_h)
	text_raw = text_raw.replace('i',E_N_i)
	text_raw = text_raw.replace('j',E_N_j)
	text_raw = text_raw.replace('k',E_N_k)
	text_raw = text_raw.replace('l',E_N_l)
	text_raw = text_raw.replace('m',E_N_m)
	text_raw = text_raw.replace('n',E_N_n)
	text_raw = text_raw.replace('o',E_N_o)
	text_raw = text_raw.replace('p',E_N_p)
	text_raw = text_raw.replace('q',E_N_q)
	text_raw = text_raw.replace('r',E_N_r)
	text_raw = text_raw.replace('s',E_N_s)
	text_raw = text_raw.replace('t',E_N_t)
	text_raw = text_raw.replace('u',E_N_u)
	text_raw = text_raw.replace('v',E_N_v)
	text_raw = text_raw.replace('w',E_N_w)
	text_raw = text_raw.replace('x',E_N_x)
	text_raw = text_raw.replace('y',E_N_y)
	text_raw = text_raw.replace('z',E_N_z)
	text_raw = text_raw.replace('A',E_N_A)
	text_raw = text_raw.replace('B',E_N_B)
	text_raw = text_raw.replace('C',E_N_C)
	text_raw = text_raw.replace('D',E_N_D)
	text_raw = text_raw.replace('E',E_N_E)
	text_raw = text_raw.replace('F',E_N_F)
	text_raw = text_raw.replace('G',E_N_G)
	text_raw = text_raw.replace('H',E_N_H)
	text_raw = text_raw.replace('I',E_N_I)
	text_raw = text_raw.replace('J',E_N_J)
	text_raw = text_raw.replace('K',E_N_K)
	text_raw = text_raw.replace('L',E_N_L)
	text_raw = text_raw.replace('M',E_N_M)
	text_raw = text_raw.replace('N',E_N_N)
	text_raw = text_raw.replace('O',E_N_O)
	text_raw = text_raw.replace('P',E_N_P)
	text_raw = text_raw.replace('Q',E_N_Q)
	text_raw = text_raw.replace('R',E_N_R)
	text_raw = text_raw.replace('S',E_N_S)
	text_raw = text_raw.replace('T',E_N_T)
	text_raw = text_raw.replace('U',E_N_U)
	text_raw = text_raw.replace('V',E_N_V)
	text_raw = text_raw.replace('W',E_N_W)
	text_raw = text_raw.replace('X',E_N_X)
	text_raw = text_raw.replace('Y',E_N_Y)
	text_raw = text_raw.replace('Z',E_N_Z)
################################################################################################################


def S_DECRYPT():
	global SD_Seperator, text_raw, text_decrypt
	os.system('title Super Decrypter && cls')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;33m')
	print('                  ╔═══════════════════╗')
	print('     ╔════════════╣\033[1;31m  Super Decrypter  \033[1;33m╠════════════╗')
	print('     ║            ╚═══════════════════╝            ║')
	print('     ║ \033[1;33m1. \033[1;36mEnter all 20 codes that secures the text \033[1;33m║')
	print('     ║       \033[1;33m2. \033[1;36mEnter the encrypted numbers        \033[1;33m║')
	print('     ║     \033[1;35m-Enter \033[1;33m"auto"\033[1;35m to change all codes-      \033[1;33m║')
	print('     ║            \033[1;31m-ENTER \033[1;33m"B"\033[1;31m TO GO BACK            \033[1;33m║')
	print('     ║        ╔════════════════════════════╗       ║')
	print('     ╚════════╣ \033[1;31m# of possible combinations\033[1;33m ╠═══════╝\033[1;33m')
	print('              ║          \033[1;36m1 Googol          \033[1;33m║')
	print('              ╚════════════════════════════╝')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	SD_Seperator = input('\033[1;36mSeperator \033[1;35m[\033[1;31mLETTERS \033[1;36m+ \033[1;31mSYMBOLS ONLY\033[1;35m]\033[1;36m: \033[1;33m')
	if len(SD_Seperator) <= 0:
		S_DECRYPT()
	CANT_PASS = '0123456789'
	for a in CANT_PASS:
		for b in SD_Seperator:
			if a == b:
				INV_OPT()
				S_DECRYPT()
	inputcode_eval_1 = input('\033[1;36mFirst code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SD_CHECKER(inputcode_eval_1)
	inputcode_1 = int(inputcode_eval_1)
	inputcode_eval_2 = input('\033[1;36mSecond code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SD_CHECKER(inputcode_eval_2)
	inputcode_2 = int(inputcode_eval_2)
	inputcode_eval_3 = input('\033[1;36mThird code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SD_CHECKER(inputcode_eval_3)
	inputcode_3 = int(inputcode_eval_3)
	inputcode_eval_4 = input('\033[1;36mFourth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SD_CHECKER(inputcode_eval_4)
	inputcode_4 = int(inputcode_eval_4)
	inputcode_eval_5 = input('\033[1;36mFifth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SD_CHECKER(inputcode_eval_5)
	inputcode_5 = int(inputcode_eval_5)
	inputcode_eval_6 = input('\033[1;36mSixth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SD_CHECKER(inputcode_eval_6)
	inputcode_6 = int(inputcode_eval_6)
	inputcode_eval_7 = input('\033[1;36mSeventh code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SD_CHECKER(inputcode_eval_7)
	inputcode_7 = int(inputcode_eval_7)
	inputcode_eval_8 = input('\033[1;36mEighth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SD_CHECKER(inputcode_eval_8)
	inputcode_8 = int(inputcode_eval_8)
	inputcode_eval_9 = input('\033[1;36mNinth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SD_CHECKER(inputcode_eval_9)
	inputcode_9 = int(inputcode_eval_9)
	inputcode_eval_10 = input('\033[1;36mTenth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SD_CHECKER(inputcode_eval_10)
	inputcode_10 = int(inputcode_eval_10)
	inputcode_eval_11 = input('\033[1;36mEleventh code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SD_CHECKER(inputcode_eval_11)
	inputcode_11 = int(inputcode_eval_11)
	inputcode_eval_13 = input('\033[1;36mTwelfth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SD_CHECKER(inputcode_eval_13)
	inputcode_13 = int(inputcode_eval_13)
	inputcode_eval_14 = input('\033[1;36mThirteenth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SD_CHECKER(inputcode_eval_14)
	inputcode_14 = int(inputcode_eval_14)
	inputcode_eval_15 = input('\033[1;36mFourteenth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SD_CHECKER(inputcode_eval_15)
	inputcode_15 = int(inputcode_eval_15)
	inputcode_eval_16 = input('\033[1;36mFifteenth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SD_CHECKER(inputcode_eval_16)
	inputcode_16 = int(inputcode_eval_16)
	inputcode_eval_17 = input('\033[1;36mSixteenth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SD_CHECKER(inputcode_eval_17)
	inputcode_17 = int(inputcode_eval_17)
	inputcode_eval_18 = input('\033[1;36mSeventeenth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SD_CHECKER(inputcode_eval_18)
	inputcode_18 = int(inputcode_eval_18)
	inputcode_eval_19 = input('\033[1;36mEighteenth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SD_CHECKER(inputcode_eval_19)
	inputcode_19 = int(inputcode_eval_19)
	inputcode_eval_20 = input('\033[1;36mNineteenth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SD_CHECKER(inputcode_eval_20)
	inputcode_20 = int(inputcode_eval_20)
	inputcode_eval_21 = input('\033[1;36mTwentieth code \033[1;35m1 ~ 100,000\033[1;36m: \033[1;33m').lower()
	SD_CHECKER(inputcode_eval_21)
	inputcode_21 = int(inputcode_eval_21)

	SD_ENDING()

def SD_ENDING():
	global text_raw, text_decrypt
	T2D()
	text_split = text_raw.split(SD_Seperator)
	text_raw = ''
	inputcode_22 = inputcode_1 + inputcode_2 * inputcode_3 + inputcode_4 - inputcode_5 - inputcode_6 + inputcode_7 * inputcode_8 + inputcode_9 - inputcode_10 - inputcode_11 + inputcode_13 * inputcode_14 + inputcode_15 - inputcode_16 - inputcode_17 + inputcode_18 * inputcode_19 + inputcode_20 - inputcode_21 
	while ("" in text_split):
		text_split.remove("")
	for x in text_split:
		text_decrypt = str(int(int(x) / inputcode_22 / 2055))
		DECRYPT_NUMBERS()
		text_raw += text_decrypt
	ENC_Output('sd')
	S_DECRYPT()

def SD_CHECKER(input_1):
	global inputcode_1, inputcode_2, inputcode_3, inputcode_4, inputcode_5, inputcode_6, inputcode_7, inputcode_8, inputcode_9, inputcode_10, inputcode_11, inputcode_13, inputcode_14, inputcode_15, inputcode_16, inputcode_17, inputcode_18, inputcode_19, inputcode_20, inputcode_21
	if input_1 == 'auto':
		AutoCode = input('\033[1;36mEnter the number for all codes: \033[1;33m')
		SD_STRINGCHECK(AutoCode)
		SD_CODECHECK(AutoCode)
		inputcode_1 = inputcode_2 = inputcode_3 = inputcode_4 = inputcode_5 = inputcode_6 = inputcode_7 = inputcode_8 = inputcode_9 = inputcode_10 = inputcode_11 = inputcode_13 = inputcode_14 = inputcode_15 = inputcode_16 = inputcode_17 = inputcode_18 = inputcode_19 = inputcode_20 = inputcode_21 = int(AutoCode)
		SD_ENDING()
	SD_STRINGCHECK(input_1)
	SD_CODECHECK(input_1)

def SD_STRINGCHECK(inputcode):
	if len(inputcode) <= 0 or inputcode.isspace() == True:
		S_DECRYPT()
	if inputcode == 'b':
		Main()
	CANT_PASS = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+|{}:"<>?`-=\\[];\',./'
	for a in CANT_PASS:
		for b in inputcode:
			if a == b:
				INV_OPT()
				S_DECRYPT()
	
def SD_CODECHECK(inputcode):
	inputcode = int(inputcode)
	if inputcode <= 0 or inputcode > 100000:
		INV_OPT()
		S_DECRYPT()
################################################################################################################


def A_DECRYPT():
	global AD_Seperator, text_raw, text_decrypt
	os.system('mode 57,20 && title Advanced Decrypter && cls')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;33m')
	print('                 ╔════════════════════╗')
	print('     ╔═══════════╣\033[1;36m Advanced \033[1;31mDecrypter \033[1;33m╠═══════════╗')
	print('     ║           ╚════════════════════╝           ║')
	print('     ║ \033[1;33m1. \033[1;36mEnter the 5 codes that secure the text  \033[1;33m║')
	print('     ║        \033[1;33m2. \033[1;36mEnter the text to encrypt        \033[1;33m║')
	print('     ║     \033[1;35m-Enter \033[1;33m"auto"\033[1;35m to change all codes-     \033[1;33m║')
	print('     ║            \033[1;31mENTER \033[1;33m"B"\033[1;31m TO GO BACK            \033[1;33m║')
	print('     ║       ╔════════════════════════════╗       ║')
	print('     ╚═══════╣ \033[1;31m# of possible combinations\033[1;33m ╠═══════╝\033[1;33m')
	print('             ║ \033[1;36m99,950,010,000,000,000,000 \033[1;33m║')
	print('             ╚════════════════════════════╝')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	AD_Seperator = input('\033[1;36mSeperator \033[1;35m[\033[1;31mLETTERS \033[1;36m+ \033[1;31mSYMBOLS ONLY\033[1;35m]\033[1;36m: \033[1;33m')
	if len(AD_Seperator) <= 0:
		A_DECRYPT()
	CANT_PASS = '0123456789'
	for a in CANT_PASS:
		for b in AD_Seperator:
			if a == b:
				INV_OPT()
				A_DECRYPT()
	inputcode_eval_1 = input('\033[1;36mFirst code \033[1;35m1 ~ 9,999\033[1;36m: \033[1;33m').lower()
	AD_CHECKER(inputcode_eval_1)
	inputcode_1 = int(inputcode_eval_1)
	inputcode_eval_2 = input('\033[1;36mSecond code \033[1;35m1 ~ 9,999\033[1;36m: \033[1;33m').lower()
	AD_CHECKER(inputcode_eval_2)
	inputcode_2 = int(inputcode_eval_2)
	inputcode_eval_3 = input('\033[1;36mThird code \033[1;35m1 ~ 9,999\033[1;36m: \033[1;33m').lower()
	AD_CHECKER(inputcode_eval_3)
	inputcode_3 = int(inputcode_eval_3)
	inputcode_eval_4 = input('\033[1;36mFourth code \033[1;35m1 ~ 9,999\033[1;36m: \033[1;33m').lower()
	AD_CHECKER(inputcode_eval_4)
	inputcode_4 = int(inputcode_eval_4)
	inputcode_eval_5 = input('\033[1;36mFifth code \033[1;35m1 ~ 9,999\033[1;36m: \033[1;33m').lower()
	AD_CHECKER(inputcode_eval_5)
	inputcode_5 = int(inputcode_eval_5)

	AD_ENDING()

def AD_ENDING():
	global text_raw, text_decrypt
	T2D()
	text_split = text_raw.split(AD_Seperator)
	text_raw = ''
	inputcode_6 = inputcode_1 + inputcode_2 * inputcode_3 + inputcode_4 * inputcode_5
	while ("" in text_split):
		text_split.remove("")
	for x in text_split:
		text_decrypt = str(int(int(x) / inputcode_6 / 2055))
		DECRYPT_NUMBERS()
		text_raw += text_decrypt
	ENC_Output('ad')
	A_DECRYPT()

def AD_CHECKER(input_1):
	global inputcode_1, inputcode_2, inputcode_3, inputcode_4, inputcode_5
	if input_1 == 'auto':
		AutoCode = input('\033[1;36mEnter the number for all codes: \033[1;33m')
		AD_STRINGCHECK(AutoCode)
		AD_CODECHECK(AutoCode)
		inputcode_1 = inputcode_2 = inputcode_3 = inputcode_4 = inputcode_5 = int(AutoCode)
		AD_ENDING()
	AD_STRINGCHECK(input_1)
	AD_CODECHECK(input_1)

def AD_STRINGCHECK(inputcode):
	if len(inputcode) <= 0 or inputcode.isspace() == True:
		A_DECRYPT()
	if inputcode == 'b':
		Main()
	CANT_PASS = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+|{}:"<>?`-=\\[];\',./'
	for a in CANT_PASS:
		for b in inputcode:
			if a == b:
				INV_OPT()
				A_DECRYPT()
	
def AD_CODECHECK(inputcode):
	inputcode = int(inputcode)
	if inputcode <= 0 or inputcode > 9999:
		INV_OPT()
		A_DECRYPT()
################################################################################################################


################################################################################################################
#                                               NORMAL DECRYPTER                                               #
################################################################################################################
def N_DECRYPT():
	global ND_Seperator, text_raw, text_decrypt, inputcode_1
	os.system('mode 57,20 && title Normal Decrypter && cls')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;33m')
	print('                 ╔════════════════════╗')
	print('     ╔═══════════╣\033[1;36m  Normal \033[1;31mDecrypter  \033[1;33m╠═══════════╗')
	print('     ║           ╚════════════════════╝           ║')
	print('     ║   \033[1;33m1. \033[1;36mEnter the code that secures the text  \033[1;33m║')
	print('     ║    \033[1;33m2. \033[1;36mEnter the text you want to encrypt   \033[1;33m║')
	print('     ║           \033[1;31m-ENTER \033[1;33m"B"\033[1;31m TO GO BACK-           \033[1;33m║')
	print('     ║       ╔════════════════════════════╗       ║')
	print('     ╚═══════╣ \033[1;31m# of possible combinations\033[1;33m ╠═══════╝\033[1;33m')
	print('             ║            \033[1;36m9,999           \033[1;33m║')
	print('             ╚════════════════════════════╝')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	ND_Seperator = input('\033[1;36mSeperator \033[1;35m[\033[1;31mLETTERS \033[1;36m+ \033[1;31mSYMBOLS ONLY\033[1;35m]\033[1;36m: \033[1;33m')
	if len(ND_Seperator) <= 0:
		N_DECRYPT()
	CANT_PASS = '0123456789'
	for a in CANT_PASS:
		for b in ND_Seperator:
			if a == b:
				INV_OPT()
				N_DECRYPT()
	inputcode_eval = input('\033[1;36mCode \033[1;35m1 ~ 9,999\033[1;36m: \033[1;33m').lower()
	if len(inputcode_eval) <= 0 or inputcode_eval.isspace() == True:
		N_DECRYPT()
	if inputcode_eval == 'b':
		Main()
	CANT_PASS = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+|{}:"<>?`-=\\[];\',./'
	for a in CANT_PASS:
		for b in inputcode_eval:
			if a == b:
				INV_OPT()
				N_DECRYPT()
	inputcode_1 = int(inputcode_eval)
	if inputcode_1 <= 0 or inputcode_1 > 9999:
		INV_OPT()
		N_DECRYPT()
	T2D()
	text_split = text_raw.split(ND_Seperator)
	text_raw = ''
	while ("" in text_split):
		text_split.remove("")
	for x in text_split:
		text_decrypt = str(int(int(x) / inputcode_1 / 2055))
		DECRYPT_NUMBERS()
		text_raw += text_decrypt
	ENC_Output('nd')
	N_DECRYPT()
################################################################################################################
#                                             MAIN DECRYPT FUNCTION                                            #
################################################################################################################
def DECRYPT_NUMBERS():
	global text_decrypt
	text_decrypt = text_decrypt.replace('107','j')
	text_decrypt = text_decrypt.replace('117','k')
	text_decrypt = text_decrypt.replace('137','l')
	text_decrypt = text_decrypt.replace('147','m')
	text_decrypt = text_decrypt.replace('157','n')
	text_decrypt = text_decrypt.replace('167','o')
	text_decrypt = text_decrypt.replace('177','p')
	text_decrypt = text_decrypt.replace('187','q')
	text_decrypt = text_decrypt.replace('197','r')
	text_decrypt = text_decrypt.replace('207','s')
	text_decrypt = text_decrypt.replace('217','t')
	text_decrypt = text_decrypt.replace('227','u')
	text_decrypt = text_decrypt.replace('237','v')
	text_decrypt = text_decrypt.replace('247','w')
	text_decrypt = text_decrypt.replace('257','x')
	text_decrypt = text_decrypt.replace('267','y')
	text_decrypt = text_decrypt.replace('277','z')
	text_decrypt = text_decrypt.replace('287','A')
	text_decrypt = text_decrypt.replace('297','B')
	text_decrypt = text_decrypt.replace('307','C')
	text_decrypt = text_decrypt.replace('317','D')
	text_decrypt = text_decrypt.replace('327','E')
	text_decrypt = text_decrypt.replace('337','F')
	text_decrypt = text_decrypt.replace('347','G')
	text_decrypt = text_decrypt.replace('357','H')
	text_decrypt = text_decrypt.replace('367','I')
	text_decrypt = text_decrypt.replace('377','J')
	text_decrypt = text_decrypt.replace('387','K')
	text_decrypt = text_decrypt.replace('397','L')
	text_decrypt = text_decrypt.replace('407','M')
	text_decrypt = text_decrypt.replace('417','N')
	text_decrypt = text_decrypt.replace('427','O')
	text_decrypt = text_decrypt.replace('437','P')
	text_decrypt = text_decrypt.replace('447','Q')
	text_decrypt = text_decrypt.replace('457','R')
	text_decrypt = text_decrypt.replace('467','S')
	text_decrypt = text_decrypt.replace('477','T')
	text_decrypt = text_decrypt.replace('487','U')
	text_decrypt = text_decrypt.replace('497','V')
	text_decrypt = text_decrypt.replace('507','W')
	text_decrypt = text_decrypt.replace('517','X')
	text_decrypt = text_decrypt.replace('527','Y')
	text_decrypt = text_decrypt.replace('537','Z')
	text_decrypt = text_decrypt.replace('17','a')
	text_decrypt = text_decrypt.replace('27','b')
	text_decrypt = text_decrypt.replace('37','c')
	text_decrypt = text_decrypt.replace('47','d')
	text_decrypt = text_decrypt.replace('57','e')
	text_decrypt = text_decrypt.replace('67','f')
	text_decrypt = text_decrypt.replace('77','g')
	text_decrypt = text_decrypt.replace('87','h')
	text_decrypt = text_decrypt.replace('97','i')
	text_decrypt = text_decrypt.replace('7',' ')
################################################################################################################


################################################################################################################
#                                           Multi-Language Translator                                          #
################################################################################################################
def MT():
	global text_raw, ALR_PASSED, MT_Lang, ALR_PASSED, MT_SF, MT_VR_ALR_PASSED
	MT_VR_ALR_PASSED = 0
	ALR_PASSED = 0
	os.system('mode 57,20 && title Multi-Language Translator && cls')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;33m')
	print('               ╔═══════════════════════════╗')
	print('     ╔═════════╣ \033[1;35mMulti-Language Translator \033[1;33m╠═════════╗')
	print('     ║         ╚═══════════════════════════╝         ║')
	print('     ║          \033[1;33m1. \033[1;36mEnter the first language          \033[1;33m║')
	print('     ║        \033[1;33m2. \033[1;36mEnter the text to translate         \033[1;33m║')
	print('     ║ \033[1;33m3. \033[1;36mChoose to save the project as you continue \033[1;33m║')
	print('     ║         \033[1;33m4. \033[1;36mEnter the second language          \033[1;33m║')
	print('     ║             \033[1;31mENTER \033[1;33m"B" \033[1;31mTO GO BACK              \033[1;33m║')
	print('     ║ ╔═══════════════════════════════════════════╗ ║')
	print('     ╚═╣ \033[1;35mENTER \033[1;33m"L" \033[1;35mAND SEE ALL AVAILABLE ALPHABETS \033[1;33m╠═╝')
	print('       ╚═══════════════════════════════════════════╝')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;33m')
	MT_Lang = input('\033[1;36mAlphabet \033[1;31m/ \033[1;36mLanguage: \033[1;33m')
	if MT_Lang == 'b':
		Main()
	if MT_Lang == 'l':
		list_langs()
		MT()
	if MT_Lang == 'rya':
		T2E()
		lang_rya()
	if MT_Lang == 'lazy':
		T2E()
		lang_lazy()
	if MT_Lang == '0x':
		T2E()
		lang_0x()
	if MT_Lang == '0xq':
		T2E()
		lang_0xq()
	if MT_Lang == 'leet':
		lang_leet()
		T2E()
		lang_leet2()
	if MT_Lang == 'binary':
		T2E()
		lang_binary()
	if MT_Lang == 'crazy':
		T2E()
		lang_crazy()
	if MT_Lang == 'crazy2':
		T2E()
		lang_crazy2()
	if MT_Lang == 'bw':
		T2E()
		lang_backwards()
	if MT_Lang == '3r':
		T2E()
		lang_3R()
	if MT_Lang == '3l':
		T2E()
		lang_3L()
	if MT_Lang == '2r':
		T2E()
		lang_2R()
	if MT_Lang == '2l':
		T2E()
		lang_2L()
	if MT_Lang == '1r':
		T2E()
		lang_1R()
	if MT_Lang == '1l':
		T2E()
		lang_1L()
	if MT_Lang == 'lc':
		T2E()
		lang_LC()
	if MT_Lang == 'uc':
		T2E()
		lang_UC()
	if MT_Lang == 'vr':
		lang_VR()
		MT_VR_ALR_PASSED = 1

	MT_AskIfSaving()

	MT_PART2()

def MT_PART2():
	global text_raw, text_raw_backup, Add_H, Add_L, MT_Saving, MT_Lang, ALR_PASSED, MT_SF, VR_UseY
	if MT_Saving == 1:
		MT_SF = MT_SF_2
		with open(MT_SF, 'a') as MT_SF:
			if Add_H == 1:
				if ALR_PASSED == 0:
					print('\n#====================================#\n#	     Created by 0xifer	     #\n#====================================#\n', file = MT_SF)
					ALR_PASSED = 1
					Add_H = 0
			if Add_L == 1:
				if MT_Lang == 'leet':
					print('\nInput = ' + text_raw_backup + '\nLanguage = ' + MT_Lang + ' / LEVEL-' + str(leet_level) + '\nOutput = ' + text_raw, file = MT_SF)
				if MT_Lang == 'vr':
					if VR_EoA == '1':
						print('\nInput = ' + text_raw_backup + '\nLanguage = ' + MT_Lang + ' - Mode = Easy', file = MT_SF)
					if VR_EoA == '2':
						print('\nInput = ' + text_raw_backup + '\nLanguage = ' + MT_Lang + ' - Mode = Advanced', file = MT_SF)
					if VR_UseUoL == '1':
						print('   Casing: LOWERCASE', file = MT_SF)
					if VR_UseUoL == '2':
						print('   Casing: UPPERCASE', file = MT_SF)
					if VR_UseUoL == '3':
						print('   Casing: LOWERCASE + UPPERCASE', file = MT_SF)
					if VR_UseY == '1':
						print('   Using Y: "y"', file = MT_SF)
					if VR_UseY == '2':
						print('   Using Y: "Y"', file = MT_SF)
					if VR_UseY == '3':
						print('   Using Y: "y" + "Y"', file = MT_SF)
					if VR_EoA == '1':
						print('   Replaced:\n    All vowels = \'' + '###VR_E_RW###' + '\'', file = MT_SF)
					if VR_EoA == '2':
						print('   Replaced:\n    a = \'' + VR_A_a_Equals + '\'\n    A = \'' + VR_A_A_Equals + '\'\n\n    e = \'' + VR_A_e_Equals + '\'\n    E = \'' + VR_A_E_Equals + '\'\n\n    i = \'' + VR_A_i_Equals + '\'\n    I = \'' + VR_A_I_Equals + '\'\n\n    o = \'' + VR_A_o_Equals + '\'\n    O = \'' + VR_A_O_Equals + '\'\n\n    u = \'' + VR_A_u_Equals + '\'\n    U = \'' + VR_A_U_Equals + '\'\n', file = MT_SF)
						if VR_UseY == '1':
							print('    y = \'' + VR_A_y_Equals + '\'', file = MT_SF)
						if VR_UseY == '2':
							print('    Y = \'' + VR_A_Y_Equals + '\'', file = MT_SF)
						if VR_UseY == '3':
							print('    y = \'' + VR_A_y_Equals + '\'\n    Y = \'' + VR_A_Y_Equals + '\'', file = MT_SF)
					print('Output = ' + text_raw, file = MT_SF)
				else:
					if MT_Lang != 'leet':
						print('\nInput = ' + text_raw_backup + '\nLanguage = ' + MT_Lang + '\nOutput = ' + text_raw, file = MT_SF)
			else:
				if MT_Lang == 'leet':
					print('\n' + text_raw_backup + '\n' + MT_Lang + '-' + str(leet_level) + '\n' + text_raw, file = MT_SF)
				else:
					print('\n' + text_raw_backup + '\n' + MT_Lang + '\n' + text_raw, file = MT_SF)
		MT_SF.close()
	ALR_PASSED = 1
	MT_PART3()

def MT_PART3():
	global MT_Lang, text_raw_backup
	os.system('title Output [MT/RMT] && cls')
	print('	   \033[1;31m╔═══════════════════\033[1;36m════════════════╗')
	print('	   \033[1;31m║        CIPHERED TE\033[1;36mXT BELOW        ║')
	print('	   \033[1;31m╚═══════════════════\033[1;36m════════════════╝')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	print('\n\033[1;33m' + text_raw + '\n')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	print('          \033[1;33m\'B\' \033[1;31mTO GO BACK \033[1;35m/ \033[1;33m\'C\' \033[1;32mTO COPY THE OUTPUT\n')
	text_raw_backup = text_raw
	MT_Lang = input('\033[1;36mNext Alphabet \033[1;31m/ \033[1;36mLanguage: \033[1;33m')
	if MT_Lang == 'b':
		MT()
	if MT_Lang == 'c':
		pyperclip.copy(text_raw)
		print('                         \033[1;36m╔════════╗')
		print('	                 ║ \033[1;33mCOPIED \033[1;36m║')
		print('	                 ╚════════╝')
		time.sleep(.7)
		MT_PART3()
	if MT_Lang == 'l':
		list_langs()
		MT_PART3()
	if MT_Lang == 'rya':
		lang_rya()
		MT_PART2()
	if MT_Lang == 'lazy':
		lang_lazy()
		MT_PART2()
	if MT_Lang == '0x':
		lang_0x()
		MT_PART2()
	if MT_Lang == '0xq':
		lang_0xq()
		MT_PART2()
	if MT_Lang == 'leet':
		lang_leet()
		lang_leet2()
		MT_PART2()
	if MT_Lang == 'binary':
		lang_binary()
		MT_PART2()
	if MT_Lang == 'crazy':
		lang_crazy()
		MT_PART2()
	if MT_Lang == 'crazy2':
		lang_crazy2()
		MT_PART2()
	if MT_Lang == 'bw':
		lang_backwards()
		MT_PART2()
	if MT_Lang == '3r':
		lang_3R()
		MT_PART2()
	if MT_Lang == '3l':
		lang_3L()
		MT_PART2()
	if MT_Lang == '2r':
		lang_2R()
		MT_PART2()
	if MT_Lang == '2l':
		lang_2L()
		MT_PART2()
	if MT_Lang == '1r':
		lang_1R()
		MT_PART2()
	if MT_Lang == '1l':
		lang_1L()
		MT_PART2()
	if MT_Lang == 'lc':
		lang_LC()
		MT_PART2()
	if MT_Lang == 'uc':
		lang_UC()
		MT_PART2()
	if MT_Lang == 'vr':
		lang_VR()
		MT_VR_ALR_PASSED = 1
		MT_PART2()

	MT_PART3()
################################################################################################################

def RMT():
	global text_raw, ALR_PASSED, MT_Lang, ALR_PASSED, MT_SF, MT_VR_ALR_PASSED
	MT_VR_ALR_PASSED = 0
	ALR_PASSED = 0
	os.system('mode 57,20 && title Reverse Multi-Language Translator && cls')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;33m')
	print('                       ╔═══════════╗')
	print('               ╔═══════╝  \033[1;31mREVERSE  \033[1;33m╚═══════╗')
	print('     ╔═════════║ \033[1;35mMulti-Language Translator \033[1;33m║═════════╗')
	print('     ║         ╚═══════════════════════════╝         ║')
	print('     ║        \033[1;33m1. \033[1;36mEnter the last language used        \033[1;33m║')
	print('     ║        \033[1;33m2. \033[1;36mEnter the text to translate         \033[1;33m║')
	print('     ║ \033[1;33m3. \033[1;36mChoose to save the project as you continue \033[1;33m║')
	print('     ║  \033[1;33m4. \033[1;36mEnter the next language, (last to first)  \033[1;33m║')
	print('     ║             \033[1;31mENTER \033[1;33m"B" \033[1;31mTO GO BACK              \033[1;33m║')
	print('     ║ ╔═══════════════════════════════════════════╗ ║')
	print('     ╚═║ \033[1;35mENTER \033[1;33m"L" \033[1;35mAND SEE ALL AVAILABLE ALPHABETS \033[1;33m║═╝')
	print('       ╚═══════════════════════════════════════════╝')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;33m')
	MT_Lang = input('\033[1;36mAlphabet \033[1;31m/ \033[1;36mLanguage: \033[1;33m').lower()
	if MT_Lang == 'b':
		Main()
	if MT_Lang == 'l':
		list_langs()
		MT()
	if MT_Lang == 'rya':
		T2D()
		lang_rya()
	if MT_Lang == 'lazy':
		T2D()
		lang_lazy()
	if MT_Lang == '0x':
		T2D()
		lang_R_0x()
	if MT_Lang == '0xq':
		T2D()
		lang_R_0xq()
	if MT_Lang == 'leet':
		lang_leet()
		T2D()
		lang_R_leet2()
	if MT_Lang == 'binary':
		T2D()
		lang_R_binary()
	if MT_Lang == 'crazy':
		T2D()
		lang_R_crazy()
	if MT_Lang == 'crazy2':
		T2D()
		lang_R_crazy2()
	if MT_Lang == 'bw':
		T2D()
		lang_backwards()
	if MT_Lang == '3r':
		T2D()
		lang_R_3L()
	if MT_Lang == '3l':
		T2D()
		lang_R_3R()
	if MT_Lang == '2r':
		T2D()
		lang_R_2L()
	if MT_Lang == '2l':
		T2D()
		lang_R_2R()
	if MT_Lang == '1r':
		T2D()
		lang_R_1L()
	if MT_Lang == '1l':
		T2D()
		lang_R_1R()
	if MT_Lang == 'lc':
		T2D()
		lang_UC()
	if MT_Lang == 'uc':
		T2D()
		lang_LC()

	MT_AskIfSaving()

	RMT_PART2()

def RMT_PART2():
	global text_raw, text_raw_backup, Add_H, Add_L, MT_Saving, MT_Lang, ALR_PASSED, MT_SF, VR_UseY
	if MT_Saving == 1:
		MT_SF = MT_SF_2
		with open(MT_SF, 'a') as MT_SF:
			if Add_H == 1:
				if ALR_PASSED == 0:
					print('\n#====================================#\n#	     Created by 0xifer	     #\n#====================================#', file = MT_SF)
					ALR_PASSED = 1
					Add_H = 0
			if Add_L == 1:
				if MT_Lang == 'leet':
					print('\nInput = ' + text_raw_backup + '\nLanguage = ' + MT_Lang + ' / LEVEL-' + str(leet_level) + '\nOutput = ' + text_raw, file = MT_SF)
				else:
					print('\nInput = ' + text_raw_backup + '\nLanguage = ' + MT_Lang + '\nOutput = ' + text_raw, file = MT_SF)
			else:
				if MT_Lang == 'leet':
					print('\n' + text_raw_backup + '\n' + MT_Lang + '-' + str(leet_level) + '\n' + text_raw, file = MT_SF)
				else:
					print('\n' + text_raw_backup + '\n' + MT_Lang + '\n' + text_raw, file = MT_SF)
		MT_SF.close()
	ALR_PASSED = 1
	RMT_PART3()

def RMT_PART3():
	global MT_Lang, text_raw_backup
	os.system('title Output [MT/RMT] && cls')
	print('	   \033[1;31m╔═══════════════════\033[1;36m════════════════╗')
	print('	   \033[1;31m║        CIPHERED TE\033[1;36mXT BELOW        ║')
	print('	   \033[1;31m╚═══════════════════\033[1;36m════════════════╝')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	print('\n\033[1;33m' + text_raw + '\n')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	print('          \033[1;33m\'B\' \033[1;31mTO GO BACK \033[1;35m/ \033[1;33m\'C\' \033[1;32mTO COPY THE OUTPUT\n')
	text_raw_backup = text_raw
	MT_Lang = input('\033[1;36mNext Alphabet \033[1;31m/ \033[1;36mLanguage: \033[1;33m').lower()
	if MT_Lang == 'b':
		RMT()
	if MT_Lang == 'c':
		pyperclip.copy(text_raw)
		print('                         \033[1;36m╔════════╗')
		print('	                 ║ \033[1;33mCOPIED \033[1;36m║')
		print('	                 ╚════════╝')
		time.sleep(.7) # Wait
		MT_PART2()
	if MT_Lang == 'l':
		list_langs()
		MT_PART3()
	if MT_Lang == 'rya':
		lang_rya()
		MT_PART2()
	if MT_Lang == 'lazy':
		lang_lazy()
		MT_PART2()
	if MT_Lang == '0x':
		lang_R_0x()
		MT_PART2()
	if MT_Lang == '0xq':
		lang_R_0xq()
		MT_PART2()
	if MT_Lang == 'leet':
		lang_leet()
		lang_R_leet2()
		MT_PART2()
	if MT_Lang == 'binary':
		lang_R_binary()
		MT_PART2()
	if MT_Lang == 'crazy':
		lang_R_crazy()
		MT_PART2()
	if MT_Lang == 'crazy2':
		lang_R_crazy2()
		MT_PART2()
	if MT_Lang == 'bw':
		lang_backwards()
		MT_PART2()
	if MT_Lang == '3r':
		lang_3L()
		MT_PART2()
	if MT_Lang == '3l':
		lang_3R()
		MT_PART2()
	if MT_Lang == '2r':
		lang_2L()
		MT_PART2()
	if MT_Lang == '2l':
		lang_2R()
		MT_PART2()
	if MT_Lang == '1r':
		lang_1L()
		MT_PART2()
	if MT_Lang == '1l':
		lang_1R()
		MT_PART2()
	if MT_Lang == 'lc':
		lang_UC()
		MT_PART2()
	if MT_Lang == 'uc':
		lang_LC()
		MT_PART2()

	RMT_PART3()
################################################################################################################

def MT_AskIfSaving():
	global MT_Saving, MT_SF, MT_SF_2, Add_H, Add_L
	MT_isSaving = input('\033[1;35mSave the output(s)? \033[1;35m[\033[1;31mY \033[1;36m/ \033[1;31mN\033[1;35m]: \033[1;33m')
	if len(MT_isSaving) <= 0 or MT_isSaving.isspace() == True:
		MT_AskIfSaving()
	if MT_isSaving == 'b':
		MT_PART3()
	if MT_isSaving.startswith('y') == True:
		MT_Saving = 1
		print('\n                \033[1;31m╔═════════\033[1;36m═════════╗')
		print('       \033[1;31m╔════════╣ CHOOSE A\033[1;36mN OPTION ╠════════╗')
		print('       \033[1;31m║        ╚═════════\033[1;36m═════════╝        ║')
		print('       \033[1;31m║    \033[1;33mR \033[1;31m= \033[1;36mReplace / Create TXT file   ║')
		print('       \033[1;31m║       \033[1;33mA \033[1;31m= \033[1;36mAdd / Create TXT file    ║')
		print('       \033[1;31m╚══════════════════\033[1;36m══════════════════╝')
		save_output = input('\033[1;36mEnter option \033[1;33m"R" \033[1;31m/ \033[1;33m"A"\033[1;36m: \033[1;33m').lower() # Ask user if they wanna replace the text file or add on to a txt file
		if save_output == "r":
			save_output_R_name = input('\033[1;36mEnter the name for this file: \033[1;33m')
			if len(save_output_R_name) <= 0 or save_output_R_name.isspace() == True:
				INV_OPT()
				MT_AskIfSaving()
			save_output_R_name = save_output_R_name
			print('\n    \033[1;35m╔════════════════════════════════════════╗')
			print('    ║    \033[1;33mDo you want to add labels for the   \033[1;35m║')
			print('    ║          \033[1;33mlanguage and the text?        \033[1;35m║')
			print('    ╚════════════════════════════════════════╝')
			print('                  \033[1;33mY \033[1;31m= \033[1;36mYes \033[1;31m/ \033[1;33mN \033[1;31m= \033[1;36mNo')
			save_output_R_labels = input('\033[1;36mAdd labels?: \033[1;33m').lower()
			if len(save_output_R_labels) <= 0 or save_output_R_labels.isspace() == True:
				INV_OPT()
				MT_AskIfSaving()
			if save_output_R_labels.startswith('y') == True:
				Add_L = 1
				Add_H = 0
			if save_output_R_labels.startswith('n') == True:
				Add_L = 0
				Add_H = 0
			SO_R_N = open(save_output_R_name, 'w')
			SO_R_N.close()
			MT_SF = save_output_R_name
			MT_SF_2 = MT_SF
		if save_output == "a":
			save_output_A_name = input('\033[1;36mEnter the name for this file: \033[1;33m')
			if len(save_output_A_name) <= 0 or save_output_A_name.isspace() == True:
				INV_OPT()
				MT_AskIfSaving()
			MT_SF = save_output_A_name
			MT_SF_2 = MT_SF
			print('\n \033[1;35m╔═══════════════════════════════════════════════╗')
			print(' ║ \033[1;33mDo you want to add a header before the output \033[1;35m║')
			print(' ║   \033[1;33minside the TXT file as a way of spotting?   \033[1;35m║')
			print(' ╚═══════════════════════════════════════════════╝')
			print('                  \033[1;33mY \033[1;31m= \033[1;36mYes \033[1;31m/ \033[1;33mN \033[1;31m= \033[1;36mNo')
			save_output_A_header = input('\033[1;36mAdd a header?: \033[1;33m').lower()
			if save_output_A_header.startswith('y') == True:
				print('\n    \033[1;35m╔════════════════════════════════════════╗')
				print('    ║    \033[1;33mDo you want to add labels for the   \033[1;35m║')
				print('    ║          \033[1;33mlanguage and the text?        \033[1;35m║')
				print('    ╚════════════════════════════════════════╝')
				print('                 \033[1;33mY \033[1;31m= \033[1;36mYes \033[1;31m/ \033[1;33mN \033[1;31m= \033[1;36mNo')
				save_output_A_header_label = input('\033[1;36mAdd labels?: \033[1;33m').lower()
				if len(save_output_A_header_label) <= 0 or save_output_A_header_label.isspace() == True:
					INV_OPT()
					MT_AskIfSaving()
				if save_output_A_header_label.startswith('y') == True:
					Add_L = 1
					Add_H = 1
				if save_output_A_header_label.startswith('n') == True:
					Add_L = 0
					Add_H = 1
			if save_output_A_header.startswith('n') == True:
				print('\n    \033[1;35m╔════════════════════════════════════════╗')
				print('    ║    \033[1;33mDo you want to add labels for the   \033[1;35m║')
				print('    ║          \033[1;33mlanguage and the text?        \033[1;35m║')
				print('    ╚════════════════════════════════════════╝')
				print('                 \033[1;33mY \033[1;31m= \033[1;36mYes \033[1;31m/ \033[1;33mN \033[1;31m= \033[1;36mNo')
				save_output_A_header_label = input('\033[1;36mAdd labels?: \033[1;33m').lower()
				if save_output_A_header_label.startswith('y') == True:
					Add_L = 1
					Add_H = 0
				if save_output_A_header_label.startswith('n') == True:
					Add_L = 0
					Add_H = 0
	if MT_isSaving.startswith('n') == True:
		Add_H = 0
		Add_L = 0
		MT_Saving = 0
################################################################################################################


################################################################################################################
#                                               ALGORITHM VIEWER                                               #
################################################################################################################
def ALG():
	os.system('mode 57,20 && title Algorithm Viewer && cls')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	print('               \033[1;33m╔════════════════════════╗')
	print('       \033[1;33m╔═══════║  \033[1;35mLanguage \033[1;33m- \033[1;35mAlgorithm\033[1;33m  ║═══════╗')
	print('       ║       ╚════════════════════════╝       ║')
	print('       ║      \033[1;36mJust enter the alphabet name      \033[1;33m║')
	print('       ║  \033[1;36mto see the technique used to make it  \033[1;33m║')
	print('       ║        ╔══════════════════════╗        ║')
	print('       ╚════════║ \033[1;31mENTER \033[1;33m"B" \033[1;31mTO GO BACK \033[1;33m║════════╝')
	print('      ╔═════════╚══════════════════════╝═════════╗')
	print('      ║ \033[1;35mENTER \033[1;33m"L" \033[1;35mTO SEE ALL AVAILABLE ALPHABETS\033[1;33m ║')
	print('      ╚══════════════════════════════════════════╝')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	alg_opt = input('\033[1;36mAlphabet: \033[1;33m')
	if alg_opt == 'b':
		Main()
	if alg_opt == 'l':
		list_langs()
		ALG()
	if alg_opt == 'rya':
		ALG_rya()
		ALG()
	if alg_opt == 'lazy':
		ALG_lazy()
		ALG()
	if alg_opt == '0x':
		ALG_0x()
		ALG()
	if alg_opt == '0xq':
		ALG_0xq()
		ALG()
	if alg_opt == 'crazy':
		ALG_crazy()
		ALG()
	if alg_opt == 'crazy2':
		ALG_crazy2()
		ALG()
	if alg_opt == 'bw':
		ALG_backwards()
		ALG()
	if alg_opt == '3r':
		ALG_3r()
		ALG()
	if alg_opt == '3l':
		ALG_3l()
		ALG()
	if alg_opt == '2r':
		ALG_2r()
		ALG()
	if alg_opt == '2l':
		ALG_2l()
		ALG()
	if alg_opt == '1r':
		ALG_1r()
		ALG()
	if alg_opt == '1l':
		ALG_1l()
		ALG()

	INV_OPT()
	ALG()

################################################################################################################

def ALG_backwards():
		os.system('mode 57,15title Algorithm Viewer - BACKWARDS && cls')
		print('                    \033[1;31m╔═════════════════╗')
		print(' ╔══════════════════╣ \033[1;36mReverse English \033[1;31m╠════════════════╗')
		print(' ║                  ╚═════════════════╝                ║')
		print(' ║ \033[1;36mZ Y X W V U T S R Q P O N M L K J I H G F E D C B A \033[1;31m║')
		print(' ╚═════════════════════════════════════════════════════╝\033[1;36m')
		getpass('\033[1;33mPress ENTER to continue...')
################################################################################################################

def ALG_rya():
	os.system('mode 65,40 && title Algorithm Viewer - RYA && cls')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	print('\n \033[1;31mAlgorithm for \033[1;33mRya \033[1;31mlanguage')
	print('\n \033[1;33m1.         \033[1;36mPut the English alphabet in a row of 4x6')
	print('\n \033[1;33m2.   \033[1;36mwith the remaining letters, (Y and Z), make and put')
	print('             Y under U and Z under W on a 7th row')
	print(' \033[1;35mEx.                         A B C D')
	print('                             E F G H')
	print('                             I J K L')
	print('                             M N O P')
	print('                             Q R S T')
	print('                             U V W X')
	print('                               Y Z')
	print('\n \033[1;33m3.   \033[1;36mTake the middle letters of the first row, (B and C)')
	print('    and replace them with the ends of the next row. The left')
	print('       middle letter will replace the left corner letter')
	print('     and the right middle letter replaces the right corner')
	print('                    Do this until the 6th row  ')
	print(' \033[1;35mEx.                 A B C D         A \033[1;33mE H \033[1;35mD')
	print('                     E F G H         \033[1;33mB I L C\033[1;35m')
	print('                     I J K L    =    \033[1;33mF M P G\033[1;35m')
	print('                     M N O P         \033[1;33mJ Q T K\033[1;35m')
	print('                     Q R S T         \033[1;33mN U X O\033[1;35m')
	print('                     U V W X         \033[1;33mR \033[1;35mV W \033[1;33mS\033[1;35m')
	print('                       Y Z             Y Z')
	print('\n \033[1;33m4. \033[1;36mNow just switch V and W with the letters under it, (Y and Z)')
	print(' \033[1;35mEx.         A E H D         A E H D         A E H D')
	print('             B I L C         B I L C         B I L C')
	print('             F M P G    =    F M P G    =    F M P G')
	print('             J Q T K         J Q T K         J Q T K')
	print('             N U X O         N U X O         N U X O')
	print('             R V W S         R \033[1;33mY \033[1;35mW S         R Y \033[1;33mZ \033[1;35mS')
	print('               Y Z             \033[1;33mV \033[1;35mZ             V \033[1;33mW')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	getpass('\033[1;33mPress ENTER to continue...')
################################################################################################################

def ALG_lazy():
	os.system('mode 65,38 && title Algorithm Viewer - LAZY && cls')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	print('\n \033[1;31mAlgorithm for \033[1;33m"Lazy" \033[1;31mlanguage')
	print('\n \033[1;33m1. \033[1;36mPut a chart that has the english alphabet in a 7x3 row')
	print('\n \033[1;33m2. \033[1;36mYou\'ll have 5 letters left over, (V, W, X, Y, Z)')
	print('   put these letters in a vertical line under "R", start with "V"')
	print('\n \033[1;33m3. \033[1;36mNow for the 1st row, (A B C D E F G), switch each letter')
	print('   with the letter on the opposite side, Ex.(A=G, B=F, C=E)')
	print('           DO NOT CHANGE THE MIDDLE LETTER, ( D )')
	print('\n \033[1;33m4. \033[1;36mDo the same thing for the second and third row')
	print('\033[1;35mEx.    A B C D E F G                       \033[1;33mG F E D C B A\033[1;35m')
	print('       H I J K L M N                       \033[1;33mN M L K J I H\033[1;35m')
	print('       O P Q R S T U           \033[1;35m=\033[1;33m           U T S R Q P O\033[1;35m')
	print('             V                                   V')
	print('             W                                   W')
	print('             X                                   X')
	print('             Y                                   Y')
	print('             Z                                   Z')
	print('\n \033[1;33m5. \033[1;36mFor the middle column, replace with opposite letter like the ')
	print('      first 3 rows, but for this one it will be vertical')
	print('         so the top=bottom, 2nd top=2nd bottom, etc.')
	print('\033[1;35mEx.        D = Z                           G F E \033[1;33mZ\033[1;35m C B A')
	print('           K = Y                           N M L \033[1;33mY\033[1;35m J I H')
	print('           R = X                           U T S \033[1;33mX\033[1;35m Q P O')
	print('           V = W               \033[1;35m=\033[1;33m                 W\033[1;35m')
	print('           W = V                                 \033[1;33mV\033[1;35m')
	print('           X = R                                 \033[1;33mR\033[1;35m')
	print('           Y = K                                 \033[1;33mK\033[1;35m')
	print('           Z = D                                 \033[1;33mD')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	getpass('\033[1;33mPress ENTER to continue...')
################################################################################################################

def ALG_0x():
	os.system('mode 65,44 && title Algorithm Viewer - 0x\'s LANGUAGE && cls')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	print('\n \033[1;31mAlgorithm for \033[1;33m"0x" \033[1;31mlanguage')
	print('\n \033[1;33m1. \033[1;36mPut a chart that has the english alphabet in a 10x2 row')
	print('\n \033[1;33m2. \033[1;36mYou\'ll have 6 letters left over, (\033[1;33mU\033[1;36m, \033[1;33mV\033[1;36m, \033[1;33mW\033[1;36m, \033[1;33mX\033[1;36m, \033[1;33mY\033[1;36m, \033[1;33mZ\033[1;36m)')
	print('    put these letters in the 3rd row, 2 spaces to the right, so')
	print('    \033[1;33mU \033[1;36mis under \033[1;33mM \033[1;36mand \033[1;33mZ \033[1;36mis under \033[1;33mR\033[1;36m, fill in missing with \033[1;33mV W X Y')
	print('\n \033[1;33m3. \033[1;36mNow for the 1st row, (\033[1;33mA B C D E F G H I J\033[1;36m)')
	print('    replace each letter with the letter on the opposite side,')
	print('    Ex.(\033[1;33mA\033[1;36m=\033[1;33mJ\033[1;36m, \033[1;33mB\033[1;36m=\033[1;33mI\033[1;36m, \033[1;33mC\033[1;36m=\033[1;33mH\033[1;36m), BUT DO NOT CHANGE THE MIDDLE LETTERS')
	print('\n \033[1;33m4. \033[1;36mDo the same thing for the 2nd row -NOT THE THIRD ROW-')
	print(' \033[1;35mEx.    A B C D E F G H I J           J I H G E F D C B A')
	print('        K L M N O P Q R S T     =     T S R Q O P N M L K')
	print('            U V W X Y Z                   U V W X Y Z')
	print('\n \033[1;33m5. \033[1;36mFor the 3rd row, take the ends, (\033[1;33mU \033[1;36mand \033[1;33mZ\033[1;36m), and replace them')
	print('       with each other opposite side/corner on the 1st row')
	print(' \033[1;35mEx.    A B C D E F G H I J           \033[1;33mZ I H G \033[1;35mE F \033[1;33mD C B U\033[1;35m')
	print('        K L M N O P Q R S T     =     \033[1;33mT S R Q \033[1;35mO P \033[1;33mN M L K\033[1;35m')
	print('            U V W X Y Z                   \033[1;33mA V \033[1;35mW X \033[1;33mY J')
	print('\n \033[1;33m6. \033[1;36mTake the inside ends, (\033[1;33mV \033[1;36mand \033[1;33mY), and replace them with')
	print('       each other opposite side/corner on the 2nd row')
	print(' \033[1;35mEx.    Z I H G E F D C B U           Z I H G E F D C B U')
	print('        T S R Q O P N M L K     =     \033[1;33mY \033[1;35mS R Q O P N M L \033[1;33mV\033[1;35m')
	print('            A V W X Y J                   A \033[1;33mK \033[1;35mW X \033[1;33mT \033[1;35mJ')
	print('\n \033[1;33m7.   \033[1;36mThe letters that didn\'t change are called middle letters.')
	print('    \033[1;33mTake the \033[1;32m1st row\'s \033[1;33mmiddle letters and shift them \033[1;32mdown 1 row')
	print('    \033[1;33mTake the \033[1;32m2nd row\'s \033[1;33mmiddle letters and shift them \033[1;32mdown 1 row')
	print('    \033[1;33mTake the \033[1;32m3rd row\'s \033[1;33mmiddle letters and shift them \033[1;32mup 2 rows.')
	print('    \033[1;33mLastly, once each row is shifted, switch the middle numbers')
	print('         with the opposite middle number for the same row')
	print(' \033[1;35mEx.    Z I H G E F D C B U           Z I H G \033[1;33mX W \033[1;35mD C B U')
	print('        Y S R Q O P N M L V     =     Y S R Q \033[1;33mF E \033[1;35mN M L V')
	print('            A V W X Y                     A K \033[1;33mP O \033[1;35mT J')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	getpass('\033[1;33mPress ENTER to continue...')
################################################################################################################

def ALG_0xq():
	os.system('mode 71,38 && title Algorithm Viewer - 0x\'s LANGUAGE - QWERTY EDITION && cls')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	print('\n \033[1;31mAlgorithm for \033[1;33m"!0xQ" \033[1;31mlanguage')
	print('\n \033[1;33m1.               \033[1;36mLook at the keyboard example below')
	print('                          \033[1;35mQ W E R T Y U I O P')
	print('                           A S D F G H J K L')
	print('                            Z X C V B N M')
	print('\n \033[1;33m2.      \033[1;36mTake each letter and translate it into 0x language')
	print(' \033[1;35mEx.        Q W E R T Y U I O P       \033[1;33mN P X M V T A B F E\033[1;35m')
	print('             A S D F G H J K L    =    \033[1;33mZ L G W D C U Y S\033[1;35m')
	print('              Z X C V B N M             \033[1;33mJ O H K I Q R\033[1;35m')
	print(' \n\033[1;33m3.        \033[1;36mNow start with the top row and assign each letter with the')
	print('   english alphabet with the new letter. Do the same thing for rows 2 and 3 ')
	print(' \033[1;35mEx.  \033[1;32m1st row \033[1;35m= English alphabet/From = A B C D E F G H I J')
	print('                  Keyboard letter/To  = \033[1;33mN P X M V T A B F E\033[1;35m')
	print('\n      \033[1;32m2nd row \033[1;35m= English alphabet/From = K L M N O P Q R S')
	print('                  Keyboard letter/To  = \033[1;33mZ L G W D C U Y S\033[1;35m')
	print('\n      \033[1;32m3rd row \033[1;35m= English alphabet/From = T U V W X Y Z')
	print('                  Keyboard letter/To  = \033[1;33mJ O H K I Q R\033[1;35m')
	print('\n \033[1;33m4. \033[1;36mSo now all your letters that were translated from normal keyboard,')
	print('          to 0x\'s keyboard, then to 0x\'s keyboard language')
	print('    \033[1;35mEx.        A = \033[1;33mN   \033[1;35mF = \033[1;33mT   \033[1;35mK = \033[1;33mZ   \033[1;35mP = \033[1;33mC   \033[1;35mU = \033[1;33mO             ')
	print('               \033[1;35mB = \033[1;33mP   \033[1;35mG = \033[1;33mA   \033[1;35mL = \033[1;33mL   \033[1;35mQ = \033[1;33mU   \033[1;35mV = \033[1;33mH')
	print('               \033[1;35mC = \033[1;33mX   \033[1;35mH = \033[1;33mB   \033[1;35mM = \033[1;33mG   \033[1;35mR = \033[1;33mY   \033[1;35mW = \033[1;33mK')
	print('               \033[1;35mD = \033[1;33mM   \033[1;35mI = \033[1;33mF   \033[1;35mN = \033[1;33mW   \033[1;35mS = \033[1;33mS   \033[1;35mX = \033[1;33mI')
	print('               \033[1;35mE = \033[1;33mV   \033[1;35mJ = \033[1;33mE   \033[1;35mO = \033[1;33mD   \033[1;35mT = \033[1;33mJ   \033[1;35mY = \033[1;33mQ')
	print('                               \033[1;35mZ = \033[1;33mR')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	getpass('\033[1;33mPress ENTER to continue...')
################################################################################################################

def ALG_crazy():
	os.system('mode 57,42 && title Algorithm Viewer - CRAZY && cls')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	print('\n \033[1;31mAlgorithm for \033[1;33m"Crazy" \033[1;31mlanguage')
	print('\n \033[1;33m1.  \033[1;36mTake A, B, C, D, and put them downward diagonally')
	print('               do the same for E, F, G, H')
	print(' \033[1;35mEx.                     A     E')
	print('                           B F ')
	print('                           G C ')
	print('                         H     D')
	print('\n \033[1;33m2. \033[1;36mFill in the gaps, continuing with the normal alphabet')
	print(' \033[1;35mEx.                     A \033[1;33mI J \033[1;35mE')
	print('                         \033[1;33mP \033[1;35mB F \033[1;33mK')
	print('                         O \033[1;35mG C \033[1;33mL')
	print('                         \033[1;35mH \033[1;33mN M \033[1;35mD')
	print('\n \033[1;33m3. \033[1;36mstart at the top, above I, and place Q, then continue')
	print('          so Q above I, R above J, and S above E')
	print('\n \033[1;33m4. \033[1;36mNow continue with the normal alphabet, (T, U, V, W)')
	print('   placing it vertically, start at the top on the right')
	print('  T Right of E, U right of K, V right of L, W right of D')
	print(' \033[1;35mEx.                      \033[1;33mQ R S')
	print('                        \033[1;35mA I J E \033[1;33mT')
	print('                        \033[1;35mP B F K \033[1;33mU')
	print('                        \033[1;35mO G C L \033[1;33mV')
	print('                        \033[1;35mH N M D \033[1;33mW')
	print('\n \033[1;33m5. \033[1;36mFor X, Y, Z, start at the bottom, and right to left,')
	print('        do the same thing that you did for Q, R, S, ')
	print('            so, X under N, Y under M, Z under D')
	print(' \033[1;35mEx.                      Q R S')
	print('                        A I J E T')
	print('                        P B F K U')
	print('                        O G C L V')
	print('                        H N M D W')
	print('                          \033[1;33mX Y Z        ')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	getpass('\033[1;33mPress ENTER to continue...')
################################################################################################################

def ALG_crazy2():
	os.system('mode 57,45 && title Algorithm Viewer - CRAZY-2 && cls')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	print('\n\033[1;31mAlgorithm for \033[1;33m"Crazy2" \033[1;31mlanguage')
	print('\n \033[1;33m1.  \033[1;36mstart with \033[1;33mA \033[1;36mand \033[1;33mB\033[1;36m, then go diagonally southeast')
	print('       and place \033[1;33mC\033[1;36m, do that once more then place \033[1;33mD')
	print(' \033[1;35mEx.                       A B')
	print('                               C')
	print('                                 D')
	print('\n \033[1;33m2.  \033[1;36mNow do the same thing, continuing with E, F, G, H')
	print('                       but reverse it')
	print(' \033[1;35mEx.                    A B     \033[1;33mF E')
	print('                            \033[1;35mC \033[1;33mG')
	print('                            H \033[1;35mD')
	print('\n \033[1;33m3.      \033[1;36mFill in the gaps with the letters below')
	print('              \033[1;33mI\033[1;36m, \033[1;33mJ\033[1;36m, \033[1;33mK\033[1;36m, \033[1;33mL\033[1;36m, \033[1;33mM\033[1;36m, \033[1;33mN\033[1;36m, \033[1;33mO\033[1;36m, \033[1;33mP\033[1;36m, \033[1;33mQ\033[1;36m, \033[1;33mR\033[1;36m')
	print('          start in the middle (between \033[1;33mB \033[1;36mand \033[1;33mF\033[1;36m)')
	print('          and place \033[1;33mI \033[1;36mnext to \033[1;33mB \033[1;36mand \033[1;33mJ \033[1;36mnext to \033[1;33mF\033[1;36m')
	print('           then create the sides with the rest')
	print('         of the alphabet (\033[1;33mK\033[1;36m, \033[1;33mL\033[1;36m, \033[1;33mM\033[1;36m, \033[1;33mN\033[1;36m, \033[1;33mO\033[1;36m, \033[1;33mP\033[1;36m, \033[1;33mQ\033[1;36m, \033[1;33mR\033[1;36m)')
	print(' \033[1;35mEx.                    A B \033[1;33mI J \033[1;35mF E')
	print('                        \033[1;33mK L \033[1;35mC G \033[1;33mM N')
	print('                        O P \033[1;35mH D \033[1;33mQ R')
	print('\n \033[1;33m4.       \033[1;36mContinue on the top left and place \033[1;33mS\033[1;36m.')
	print('           Now goto the top right and place \033[1;33mT\033[1;36m.')
	print('             Do this on line 2 with \033[1;33mU \033[1;36mand \033[1;33mV\033[1;36m')
	print('               and on line 3 with \033[1;33mW \033[1;36mand \033[1;33mX')
	print('            For \033[1;33mY \033[1;36mand \033[1;33mZ\033[1;36m, place them under the')
	print('          middle letters. \033[1;33mY \033[1;31munder \033[1;33mH\033[1;36m, \033[1;33mZ \033[1;31munder \033[1;33mD\033[1;36m')
	print('       The new alphabet starts how you\'d read it')
	print('                  (A = \033[1;33mS\033[1;36m, B = \033[1;33mA\033[1;36m, C = \033[1;33mB\033[1;36m)')
	print(' \033[1;35m                     \033[1;33mS\033[1;35m A B I J F E \033[1;33mT')
	print('                      \033[1;33mU\033[1;35m K L C G M N \033[1;33mV')
	print('                      \033[1;33mW\033[1;35m O P H D Q R \033[1;33mX')
	print('                            Y Z')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	getpass('\033[1;33mPress ENTER to continue...')
################################################################################################################

def ALG_3r():
	os.system('mode 65,15 && title Algorithm Viewer - 3-RIGHT && cls')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	print('\n \033[1;31mAlgorithm for \033[1;33m"3R" \033[1;31mlanguage')
	print('\n \033[1;33m1. \033[1;36mTake each letter and shift it 3 letters to the right')
	print(' \033[1;35mEx. (\033[1;33mA \033[1;35mB C \033[1;33mD \033[1;35mE F G)')
	print('   \033[1;33mFROM     TO')
	print('\n \033[1;33m2. \033[1;36mOnce you get to X, you cant move it right 3 ')
	print('    because it goes past the 26th letter, so it goes to A')
	print(' \033[1;35mEx. (\033[1;33mA\033[1;35mBCDEFGHIJKLMNOPQRSTUVWXYZ\033[1;33mX\033[1;35mYZ)')
	print('     \033[1;33mTO                         FROM')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	getpass('\033[1;33mPress ENTER to continue...')
################################################################################################################

def ALG_3l():
	os.system('mode 65,15 && title Algorithm Viewer - 3-LEFT && cls')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	print('\n \033[1;31mAlgorithm for \033[1;33m"3L" \033[1;31mlanguage')
	print('\n \033[1;33m1. \033[1;36mTake each letter and shift it 3 letters to the left')
	print(' \033[1;35mEx. (\033[1;33mA \033[1;35mB C \033[1;33mD \033[1;35mE F G)')
	print('     \033[1;33mTO     FROM')
	print('\n \033[1;33m2. \033[1;36mOnce you get to C, you cant move it left 3 ')
	print('    because it goes past/before the 1st letter, so it goes to Z')
	print(' \033[1;35mEx. (AB\033[1;33mC\033[1;35mDEFGHIJKLMNOPQRSTUVWXYZXY\033[1;33mZ\033[1;35m)')
	print('     \033[1;33mFROM                         TO')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	getpass('\033[1;33mPress ENTER to continue...')
################################################################################################################

def ALG_2r():
	os.system('mode 65,15 && title Algorithm Viewer - 2-RIGHT && cls')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	print('\n \033[1;31mAlgorithm for \033[1;33m"2R" \033[1;31mlanguage')
	print('\n \033[1;33m1. \033[1;36mTake each letter and shift it 2 letters to the right')
	print(' \033[1;35mEx. (\033[1;33mA \033[1;35mB \033[1;33mC \033[1;35mD E F G)')
	print('   \033[1;33mFROM   TO')
	print('\n \033[1;33m2. \033[1;36mOnce you get to Y, you cant move it right 2 ')
	print('    because it goes past the 26th letter, so it goes to A')
	print(' \033[1;35mEx. (\033[1;33mA\033[1;35mBCDEFGHIJKLMNOPQRSTUVWXYZX\033[1;33mY\033[1;35mZ)')
	print('     \033[1;33mTO                          FROM')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	getpass('\033[1;33mPress ENTER to continue...')
################################################################################################################

def ALG_2l():
	os.system('mode 65,15 && title Algorithm Viewer - 2-LEFT && cls')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	print('\n \033[1;31mAlgorithm for \033[1;33m"2L" \033[1;31mlanguage')
	print('\n \033[1;33m1. \033[1;36mTake each letter and shift it 2 letters to the left')
	print(' \033[1;35mEx. (\033[1;33mA \033[1;35mB \033[1;33mC \033[1;35mD E F G)')
	print('     \033[1;33mTO   FROM')
	print('\n \033[1;33m2. \033[1;36mOnce you get to B, you cant move it left 2 ')
	print('    because it goes past/before the 1st letter, so it goes to Z')
	print(' \033[1;35mEx. (\033[1;33mA\033[1;35mBCDEFGHIJKLMNOPQRSTUVWXYZX\033[1;33mY\033[1;35mZ)')
	print('   \033[1;33mFROM                          TO')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	getpass('\033[1;33mPress ENTER to continue...')
################################################################################################################

def ALG_1r():
	os.system('mode 65,15 && title Algorithm Viewer - 1-RIGHT && cls')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	print('\n \033[1;31mAlgorithm for \033[1;33m"1R" \033[1;31mlanguage')
	print('\n \033[1;33m1. \033[1;36mTake each letter and shift it 1 letter to the right')
	print(' \033[1;35mEx. (\033[1;33mA B \033[1;35mC D E F G)')
	print('   \033[1;33mFROM TO')
	print('\n \033[1;33m2. \033[1;36mOnce you get to Z, you cant move it right 1 ')
	print('    because it goes past the 26th letter, so it goes to A')
	print(' \033[1;35mEx. (\033[1;33mA\033[1;35mBCDEFGHIJKLMNOPQRSTUVWXYZXY\033[1;33mZ\033[1;35m)')
	print('     \033[1;33mTO                           FROM')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	getpass('\033[1;33mPress ENTER to continue...')
################################################################################################################

def ALG_1l():
	os.system('mode 65,15 && title Algorithm Viewer - 1-LEFT && cls')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	print('\n \033[1;31mAlgorithm for \033[1;33m"!laa!" \033[1;31mlanguage')
	print('\n \033[1;33m1. \033[1;36mTake each letter and shift it 1 letter to the left')
	print(' \033[1;35mEx. (\033[1;33mA B \033[1;35mC D E F G)')
	print('     \033[1;33mTO FROM')
	print('\n \033[1;33m2. \033[1;36mOnce you get to A, you cant move it left 1 ')
	print('    because it goes past/before the 1st letter, so it goes to Z')
	print(' \033[1;35mEx. (\033[1;33mA\033[1;35mBCDEFGHIJKLMNOPQRSTUVWXYZXY\033[1;33mZ\033[1;35m)')
	print('   \033[1;33mFROM                           TO')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	getpass('\033[1;33mPress ENTER to continue...')
################################################################################################################


################################################################################################################
#                                                 RYA LANGUAGE                                                 #
################################################################################################################
def lang_rya():
	global text_raw
	text_raw = text_raw.replace('b',' #00#00# ')
	text_raw = text_raw.replace('c',' #00#01# ')
	text_raw = text_raw.replace('e','b')
	text_raw = text_raw.replace('f',' #00#02# ')
	text_raw = text_raw.replace('g',' #00#03# ')
	text_raw = text_raw.replace('h','c')
	text_raw = text_raw.replace('i','f')
	text_raw = text_raw.replace('j',' #00#04# ')
	text_raw = text_raw.replace('k',' #00#05# ')
	text_raw = text_raw.replace('l','g')
	text_raw = text_raw.replace('m','j')
	text_raw = text_raw.replace('n',' #00#06# ')
	text_raw = text_raw.replace('o',' #00#07# ')
	text_raw = text_raw.replace('p','k')
	text_raw = text_raw.replace('q','n')
	text_raw = text_raw.replace('r',' #00#08# ')
	text_raw = text_raw.replace('s',' #00#09# ')
	text_raw = text_raw.replace('t','o')
	text_raw = text_raw.replace('u','r')
	text_raw = text_raw.replace('v',' #00#10# ')
	text_raw = text_raw.replace('w',' #00#11# ')
	text_raw = text_raw.replace('x','s')
	text_raw = text_raw.replace('y','v')
	text_raw = text_raw.replace('z','w')
	text_raw = text_raw.replace('B',' #00#13# ')
	text_raw = text_raw.replace('C',' #00#14# ')
	text_raw = text_raw.replace('E','B')
	text_raw = text_raw.replace('F',' #00#15# ')
	text_raw = text_raw.replace('G',' #00#16# ')
	text_raw = text_raw.replace('H','C')
	text_raw = text_raw.replace('I','F')
	text_raw = text_raw.replace('J',' #00#17# ')
	text_raw = text_raw.replace('K',' #00#18# ')
	text_raw = text_raw.replace('L','G')
	text_raw = text_raw.replace('M','J')
	text_raw = text_raw.replace('N',' #00#19# ')
	text_raw = text_raw.replace('O',' #00#20# ')
	text_raw = text_raw.replace('P','K')
	text_raw = text_raw.replace('Q','N')
	text_raw = text_raw.replace('R',' #00#21# ')
	text_raw = text_raw.replace('S',' #00#22# ')
	text_raw = text_raw.replace('T','O')
	text_raw = text_raw.replace('U','R')
	text_raw = text_raw.replace('V',' #00#23# ')
	text_raw = text_raw.replace('W',' #00#24# ')
	text_raw = text_raw.replace('X','S')
	text_raw = text_raw.replace('Y','V')
	text_raw = text_raw.replace('Z','W')
	text_raw = text_raw.replace(' #00#00# ','e')
	text_raw = text_raw.replace(' #00#01# ','h')
	text_raw = text_raw.replace(' #00#02# ','i')
	text_raw = text_raw.replace(' #00#03# ','l')
	text_raw = text_raw.replace(' #00#04# ','m')
	text_raw = text_raw.replace(' #00#05# ','p')
	text_raw = text_raw.replace(' #00#06# ','q')
	text_raw = text_raw.replace(' #00#07# ','t')
	text_raw = text_raw.replace(' #00#08# ','u')
	text_raw = text_raw.replace(' #00#09# ','x')
	text_raw = text_raw.replace(' #00#10# ','y')
	text_raw = text_raw.replace(' #00#11# ','z')
	text_raw = text_raw.replace(' #00#13# ','E')
	text_raw = text_raw.replace(' #00#14# ','H')
	text_raw = text_raw.replace(' #00#15# ','I')
	text_raw = text_raw.replace(' #00#16# ','L')
	text_raw = text_raw.replace(' #00#17# ','M')
	text_raw = text_raw.replace(' #00#18# ','P')
	text_raw = text_raw.replace(' #00#19# ','Q')
	text_raw = text_raw.replace(' #00#20# ','T')
	text_raw = text_raw.replace(' #00#21# ','U')
	text_raw = text_raw.replace(' #00#22# ','X')
	text_raw = text_raw.replace(' #00#23# ','Y')
	text_raw = text_raw.replace(' #00#24# ','Z')
################################################################################################################


################################################################################################################
#                                                 LAZY LANGUAGE                                                #
################################################################################################################
def lang_lazy():
	global text_raw
	text_raw = text_raw.replace('e',' #00#00# ')
	text_raw = text_raw.replace('a',' #00#01# ')
	text_raw = text_raw.replace('f',' #00#02# ')
	text_raw = text_raw.replace('b','f')
	text_raw = text_raw.replace('c','e')
	text_raw = text_raw.replace('z',' #00#03# ')
	text_raw = text_raw.replace('d','z')
	text_raw = text_raw.replace('g','a')
	text_raw = text_raw.replace('n',' #00#04# ')
	text_raw = text_raw.replace('h','n')
	text_raw = text_raw.replace('m',' #00#05# ')
	text_raw = text_raw.replace('i','m')
	text_raw = text_raw.replace('l',' #00#06# ')
	text_raw = text_raw.replace('j','l')
	text_raw = text_raw.replace('y',' #00#07# ')
	text_raw = text_raw.replace('k','y')
	text_raw = text_raw.replace('u',' #00#08# ')
	text_raw = text_raw.replace('o','u')
	text_raw = text_raw.replace('t',' #00#09# ')
	text_raw = text_raw.replace('p','t')
	text_raw = text_raw.replace('s',' #00#10# ')
	text_raw = text_raw.replace('q','s')
	text_raw = text_raw.replace('x',' #00#11# ')
	text_raw = text_raw.replace('r','x')
	text_raw = text_raw.replace('w',' #00#13# ')
	text_raw = text_raw.replace('v','w')
	text_raw = text_raw.replace('E',' #00#14# ')
	text_raw = text_raw.replace('A',' #00#15# ')
	text_raw = text_raw.replace('F',' #00#16# ')
	text_raw = text_raw.replace('B','f')
	text_raw = text_raw.replace('C','e')
	text_raw = text_raw.replace('Z',' #00#17# ')
	text_raw = text_raw.replace('D','z')
	text_raw = text_raw.replace('G','a')
	text_raw = text_raw.replace('N',' #00#18# ')
	text_raw = text_raw.replace('H','n')
	text_raw = text_raw.replace('M',' #00#19# ')
	text_raw = text_raw.replace('I','m')
	text_raw = text_raw.replace('L',' #00#20# ')
	text_raw = text_raw.replace('J','l')
	text_raw = text_raw.replace('Y',' #00#21# ')
	text_raw = text_raw.replace('K','y')
	text_raw = text_raw.replace('U',' #00#22# ')
	text_raw = text_raw.replace('O','u')
	text_raw = text_raw.replace('T',' #00#23# ')
	text_raw = text_raw.replace('P','t')
	text_raw = text_raw.replace('S',' #00#24# ')
	text_raw = text_raw.replace('Q','s')
	text_raw = text_raw.replace('X',' #00#25# ')
	text_raw = text_raw.replace('R','x')
	text_raw = text_raw.replace('W',' #00#26# ')
	text_raw = text_raw.replace('V','w')
	text_raw = text_raw.replace(' #00#00# ','c')
	text_raw = text_raw.replace(' #00#01# ','g')
	text_raw = text_raw.replace(' #00#02# ','b')
	text_raw = text_raw.replace(' #00#03# ','d')
	text_raw = text_raw.replace(' #00#04# ','h')
	text_raw = text_raw.replace(' #00#05# ','i')
	text_raw = text_raw.replace(' #00#06# ','j')
	text_raw = text_raw.replace(' #00#07# ','k')
	text_raw = text_raw.replace(' #00#08# ','o')
	text_raw = text_raw.replace(' #00#09# ','p')
	text_raw = text_raw.replace(' #00#10# ','q')
	text_raw = text_raw.replace(' #00#11# ','r')
	text_raw = text_raw.replace(' #00#13# ','v')
	text_raw = text_raw.replace(' #00#14# ','C')
	text_raw = text_raw.replace(' #00#15# ','G')
	text_raw = text_raw.replace(' #00#16# ','B')
	text_raw = text_raw.replace(' #00#17# ','D')
	text_raw = text_raw.replace(' #00#18# ','H')
	text_raw = text_raw.replace(' #00#19# ','I')
	text_raw = text_raw.replace(' #00#20# ','J')
	text_raw = text_raw.replace(' #00#21# ','K')
	text_raw = text_raw.replace(' #00#22# ','O')
	text_raw = text_raw.replace(' #00#23# ','P')
	text_raw = text_raw.replace(' #00#24# ','Q')
	text_raw = text_raw.replace(' #00#25# ','R')
	text_raw = text_raw.replace(' #00#26# ','V')
################################################################################################################


################################################################################################################
#                                                 0x's LANGUAGE                                                #
################################################################################################################
def lang_0x():
	global text_raw
	text_raw = text_raw.replace('u',' #00#00# ')
	text_raw = text_raw.replace('j','u')
	text_raw = text_raw.replace('z','j')
	text_raw = text_raw.replace('a','z')
	text_raw = text_raw.replace('b',' #00#01# ')
	text_raw = text_raw.replace('c',' #00#02# ')
	text_raw = text_raw.replace('d',' #00#03# ')
	text_raw = text_raw.replace('p',' #00#04# ')
	text_raw = text_raw.replace('w','p')
	text_raw = text_raw.replace('f','w')
	text_raw = text_raw.replace('o','f')
	text_raw = text_raw.replace('x','o')
	text_raw = text_raw.replace('e','x')
	text_raw = text_raw.replace('g','d')
	text_raw = text_raw.replace('h','c')
	text_raw = text_raw.replace('i','b')
	text_raw = text_raw.replace('v',' #00#05# ')
	text_raw = text_raw.replace('t','v')
	text_raw = text_raw.replace('y','t')
	text_raw = text_raw.replace('k','y')
	text_raw = text_raw.replace('l',' #00#06# ')
	text_raw = text_raw.replace('m',' #00#07# ')
	text_raw = text_raw.replace('n',' #00#08# ')
	text_raw = text_raw.replace('q','n')
	text_raw = text_raw.replace('r','m')
	text_raw = text_raw.replace('s','l')
	text_raw = text_raw.replace('U',' #00#09# ')
	text_raw = text_raw.replace('J','U')
	text_raw = text_raw.replace('Z','J')
	text_raw = text_raw.replace('A','Z')
	text_raw = text_raw.replace('B',' #00#10# ')
	text_raw = text_raw.replace('C',' #00#11# ')
	text_raw = text_raw.replace('D',' #00#12# ')
	text_raw = text_raw.replace('P',' #00#13# ')
	text_raw = text_raw.replace('W','P')
	text_raw = text_raw.replace('F','W')
	text_raw = text_raw.replace('O','F')
	text_raw = text_raw.replace('X','O')
	text_raw = text_raw.replace('E','X')
	text_raw = text_raw.replace('G','D')
	text_raw = text_raw.replace('H','C')
	text_raw = text_raw.replace('I','B')
	text_raw = text_raw.replace('V',' #00#14# ')
	text_raw = text_raw.replace('T','V')
	text_raw = text_raw.replace('Y','T')
	text_raw = text_raw.replace('K','Y')
	text_raw = text_raw.replace('L',' #00#15# ')
	text_raw = text_raw.replace('M',' #00#16# ')
	text_raw = text_raw.replace('N',' #00#17# ')
	text_raw = text_raw.replace('Q','N')
	text_raw = text_raw.replace('R','M')
	text_raw = text_raw.replace('S','L')
	text_raw = text_raw.replace(' #00#00# ','a')
	text_raw = text_raw.replace(' #00#01# ','i')
	text_raw = text_raw.replace(' #00#02# ','h')
	text_raw = text_raw.replace(' #00#03# ','g')
	text_raw = text_raw.replace(' #00#04# ','e')
	text_raw = text_raw.replace(' #00#05# ','k')
	text_raw = text_raw.replace(' #00#06# ','s')
	text_raw = text_raw.replace(' #00#07# ','r')
	text_raw = text_raw.replace(' #00#08# ','q')
	text_raw = text_raw.replace(' #00#09# ','A')
	text_raw = text_raw.replace(' #00#10# ','I')
	text_raw = text_raw.replace(' #00#11# ','H')
	text_raw = text_raw.replace(' #00#12# ','G')
	text_raw = text_raw.replace(' #00#13# ','E')
	text_raw = text_raw.replace(' #00#14# ','K')
	text_raw = text_raw.replace(' #00#15# ','S')
	text_raw = text_raw.replace(' #00#16# ','R')
	text_raw = text_raw.replace(' #00#17# ','Q')
################################################################################################################

def lang_R_0x():
	global text_raw
	text_raw = text_raw.replace('j',' #00#00# ')
	text_raw = text_raw.replace('u','j')
	text_raw = text_raw.replace('a','u')
	text_raw = text_raw.replace('z','a')
	text_raw = text_raw.replace('b',' #00#01# ')
	text_raw = text_raw.replace('i','b')
	text_raw = text_raw.replace('c',' #00#02# ')
	text_raw = text_raw.replace('h','c')
	text_raw = text_raw.replace('p',' #00#03# ')
	text_raw = text_raw.replace('e','p')
	text_raw = text_raw.replace('x','e')
	text_raw = text_raw.replace('o','x')
	text_raw = text_raw.replace('f','o')
	text_raw = text_raw.replace('w','f')
	text_raw = text_raw.replace('g',' #00#04# ')
	text_raw = text_raw.replace('d','g')
	text_raw = text_raw.replace('t',' #00#05# ')
	text_raw = text_raw.replace('v','t')
	text_raw = text_raw.replace('k','v')
	text_raw = text_raw.replace('y','k')
	text_raw = text_raw.replace('q',' #00#06# ')
	text_raw = text_raw.replace('r',' #00#07# ')
	text_raw = text_raw.replace('s',' #00#08# ')
	text_raw = text_raw.replace('n','q')
	text_raw = text_raw.replace('m','r')
	text_raw = text_raw.replace('l','s')
	text_raw = text_raw.replace('J',' #00#09# ')
	text_raw = text_raw.replace('U','J')
	text_raw = text_raw.replace('A','U')
	text_raw = text_raw.replace('Z','A')
	text_raw = text_raw.replace('B',' #00#10# ')
	text_raw = text_raw.replace('I','B')
	text_raw = text_raw.replace('C',' #00#11# ')
	text_raw = text_raw.replace('H','C')
	text_raw = text_raw.replace('P',' #00#13# ')
	text_raw = text_raw.replace('E','P')
	text_raw = text_raw.replace('X','E')
	text_raw = text_raw.replace('O','X')
	text_raw = text_raw.replace('F','O')
	text_raw = text_raw.replace('W','F')
	text_raw = text_raw.replace('G',' #00#14# ')
	text_raw = text_raw.replace('D','G')
	text_raw = text_raw.replace('T',' #00#15# ')
	text_raw = text_raw.replace('V','T')
	text_raw = text_raw.replace('K','V')
	text_raw = text_raw.replace('Y','K')
	text_raw = text_raw.replace('Q',' #00#16# ')
	text_raw = text_raw.replace('R',' #00#17# ')
	text_raw = text_raw.replace('S',' #00#18# ')
	text_raw = text_raw.replace('N','Q')
	text_raw = text_raw.replace('M','R')
	text_raw = text_raw.replace('L','S')
	text_raw = text_raw.replace(' #00#00# ','z')
	text_raw = text_raw.replace(' #00#01# ','i')
	text_raw = text_raw.replace(' #00#02# ','h')
	text_raw = text_raw.replace(' #00#03# ','w')
	text_raw = text_raw.replace(' #00#04# ','d')
	text_raw = text_raw.replace(' #00#05# ','y')
	text_raw = text_raw.replace(' #00#06# ','n')
	text_raw = text_raw.replace(' #00#07# ','m')
	text_raw = text_raw.replace(' #00#08# ','l')
	text_raw = text_raw.replace(' #00#09# ','Z')
	text_raw = text_raw.replace(' #00#10# ','I')
	text_raw = text_raw.replace(' #00#11# ','H')
	text_raw = text_raw.replace(' #00#13# ','W')
	text_raw = text_raw.replace(' #00#14# ','D')
	text_raw = text_raw.replace(' #00#15# ','Y')
	text_raw = text_raw.replace(' #00#16# ','N')
	text_raw = text_raw.replace(' #00#17# ','M')
	text_raw = text_raw.replace(' #00#18# ','L')
################################################################################################################


################################################################################################################
#                                        0x's LANGUAGE - QWERTY EDITION                                        #
################################################################################################################
def lang_0xq():
	global text_raw
	text_raw = text_raw.replace('g',' #00#00# ')
	text_raw = text_raw.replace('m','g')
	text_raw = text_raw.replace('d','m')
	text_raw = text_raw.replace('o','d')
	text_raw = text_raw.replace('u','o')
	text_raw = text_raw.replace('q','u')
	text_raw = text_raw.replace('y','q')
	text_raw = text_raw.replace('r','y')
	text_raw = text_raw.replace('z','r')
	text_raw = text_raw.replace('k','z')
	text_raw = text_raw.replace('w','k')
	text_raw = text_raw.replace('n','w')
	text_raw = text_raw.replace('a','n')
	text_raw = text_raw.replace('h',' #00#01# ')
	text_raw = text_raw.replace('v','h')
	text_raw = text_raw.replace('e','v')
	text_raw = text_raw.replace('j','e')
	text_raw = text_raw.replace('t','j')
	text_raw = text_raw.replace('f','t')
	text_raw = text_raw.replace('i','f')
	text_raw = text_raw.replace('x','i')
	text_raw = text_raw.replace('c','x')
	text_raw = text_raw.replace('p','c')
	text_raw = text_raw.replace('b','p')
	text_raw = text_raw.replace('G',' #00#02# ')
	text_raw = text_raw.replace('M','G')
	text_raw = text_raw.replace('D','M')
	text_raw = text_raw.replace('O','D')
	text_raw = text_raw.replace('U','O')
	text_raw = text_raw.replace('Q','U')
	text_raw = text_raw.replace('Y','Q')
	text_raw = text_raw.replace('R','Y')
	text_raw = text_raw.replace('Z','R')
	text_raw = text_raw.replace('K','Z')
	text_raw = text_raw.replace('W','K')
	text_raw = text_raw.replace('N','W')
	text_raw = text_raw.replace('A','N')
	text_raw = text_raw.replace('H',' #00#03# ')
	text_raw = text_raw.replace('V','H')
	text_raw = text_raw.replace('E','V')
	text_raw = text_raw.replace('J','E')
	text_raw = text_raw.replace('T','J')
	text_raw = text_raw.replace('F','T')
	text_raw = text_raw.replace('I','F')
	text_raw = text_raw.replace('X','I')
	text_raw = text_raw.replace('C','X')
	text_raw = text_raw.replace('P','C')
	text_raw = text_raw.replace('B','P')
	text_raw = text_raw.replace(' #00#00# ','a')
	text_raw = text_raw.replace(' #00#01# ','b')
	text_raw = text_raw.replace(' #00#02# ','A')
	text_raw = text_raw.replace(' #00#03# ','B')
################################################################################################################

def lang_R_0xq():
	global text_raw
	text_raw = text_raw.replace('w',' #00#00# ')
	text_raw = text_raw.replace('k','w')
	text_raw = text_raw.replace('z','k')
	text_raw = text_raw.replace('r','z')
	text_raw = text_raw.replace('y','r')
	text_raw = text_raw.replace('q','y')
	text_raw = text_raw.replace('u','q')
	text_raw = text_raw.replace('o','u')
	text_raw = text_raw.replace('d','o')
	text_raw = text_raw.replace('m','d')
	text_raw = text_raw.replace('g','m')
	text_raw = text_raw.replace('a','g')
	text_raw = text_raw.replace('n','a')
	text_raw = text_raw.replace('c',' #00#01# ')
	text_raw = text_raw.replace('x','c')
	text_raw = text_raw.replace('i','x')
	text_raw = text_raw.replace('f','i')
	text_raw = text_raw.replace('t','f')
	text_raw = text_raw.replace('j','t')
	text_raw = text_raw.replace('e','j')
	text_raw = text_raw.replace('v','e')
	text_raw = text_raw.replace('h','v')
	text_raw = text_raw.replace('b','h')
	text_raw = text_raw.replace('p','b')
	text_raw = text_raw.replace('W',' #00#02# ')
	text_raw = text_raw.replace('K','W')
	text_raw = text_raw.replace('Z','K')
	text_raw = text_raw.replace('R','Z')
	text_raw = text_raw.replace('Y','R')
	text_raw = text_raw.replace('Q','Y')
	text_raw = text_raw.replace('U','Q')
	text_raw = text_raw.replace('C','U')
	text_raw = text_raw.replace('D','O')
	text_raw = text_raw.replace('M','D')
	text_raw = text_raw.replace('G','M')
	text_raw = text_raw.replace('A','G')
	text_raw = text_raw.replace('N','A')
	text_raw = text_raw.replace('C',' #00#03# ')
	text_raw = text_raw.replace('X','C')
	text_raw = text_raw.replace('I','X')
	text_raw = text_raw.replace('F','I')
	text_raw = text_raw.replace('T','F')
	text_raw = text_raw.replace('J','T')
	text_raw = text_raw.replace('E','J')
	text_raw = text_raw.replace('V','E')
	text_raw = text_raw.replace('H','V')
	text_raw = text_raw.replace('B','H')
	text_raw = text_raw.replace('P','B')
	text_raw = text_raw.replace(' #00#00# ','n')
	text_raw = text_raw.replace(' #00#01# ','p')
	text_raw = text_raw.replace(' #00#02# ','N')
	text_raw = text_raw.replace(' #00#03# ','P')
################################################################################################################


################################################################################################################
#                                                  1337 5P34K                                                  #
################################################################################################################
def lang_leet():
	global text_raw, leet_level
	canpass = 0
	while canpass == 0:
		os.system('cls')
		print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
		print('                 \033[1;33m╔══════════════════╗')
		print('            ╔════║ \033[1;31mCHOOSE THE LEVEL \033[1;33m║════╗')
		print('            ║    ╚══════════════════╝    ║')
		print('            ║     \033[1;36mLEVEL-\033[1;33m1  \033[1;35m/\033[1;36m  LEVEL-\033[1;33m2    ║')
		print('            ║           \033[1;36mLEVEL-\033[1;33m3          ║')
		print('            ╚════════════════════════════╝')
		print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
		leet_level = int(input('\033[1;36mLevel: \033[1;33m'))
		if leet_level == 1 or leet_level == 2 or leet_level == 3:
			canpass = 1

def lang_leet2():
	global text_raw, leet_level
	if leet_level == 1:
		text_raw = text_raw.replace('a','4')
		text_raw = text_raw.replace('b','8')
		text_raw = text_raw.replace('e','3')
		text_raw = text_raw.replace('g','9')
		text_raw = text_raw.replace('l','1')
		text_raw = text_raw.replace('o','0')
		text_raw = text_raw.replace('s','5')
		text_raw = text_raw.replace('t','7')
		text_raw = text_raw.replace('z','2')
		text_raw = text_raw.replace('A','4')
		text_raw = text_raw.replace('B','8')
		text_raw = text_raw.replace('E','3')
		text_raw = text_raw.replace('G','9')
		text_raw = text_raw.replace('L','1')
		text_raw = text_raw.replace('O','0')
		text_raw = text_raw.replace('S','5')
		text_raw = text_raw.replace('T','7')
		text_raw = text_raw.replace('Z','2')
	if leet_level == 2:
		text_raw = text_raw.replace('a','/-\\')
		text_raw = text_raw.replace('b','|3')
		text_raw = text_raw.replace('c','(')
		text_raw = text_raw.replace('d','[)')
		text_raw = text_raw.replace('e','[-')
		text_raw = text_raw.replace('g','9')
		text_raw = text_raw.replace('h','|-|')
		text_raw = text_raw.replace('j','_|')
		text_raw = text_raw.replace('k','|<')
		text_raw = text_raw.replace('m','|\\/|')
		text_raw = text_raw.replace('n','/\\/')
		text_raw = text_raw.replace('o','0')
		text_raw = text_raw.replace('p','|*')
		text_raw = text_raw.replace('q','(_,)')
		text_raw = text_raw.replace('r','/-')
		text_raw = text_raw.replace('s','$')
		text_raw = text_raw.replace('t','\'|\'')
		text_raw = text_raw.replace('u','|_|')
		text_raw = text_raw.replace('v','|/')
		text_raw = text_raw.replace('w','\\|/')
		text_raw = text_raw.replace('x',')(')
		text_raw = text_raw.replace('y','`\\')
		text_raw = text_raw.replace('z','7_')
		text_raw = text_raw.replace('A','/-\\')
		text_raw = text_raw.replace('B','|3')
		text_raw = text_raw.replace('C','(')
		text_raw = text_raw.replace('D','[)')
		text_raw = text_raw.replace('E','[-')
		text_raw = text_raw.replace('G','9')
		text_raw = text_raw.replace('H','|-|')
		text_raw = text_raw.replace('J','_|')
		text_raw = text_raw.replace('K','|<')
		text_raw = text_raw.replace('L','1')
		text_raw = text_raw.replace('M','|\\/|')
		text_raw = text_raw.replace('N','/\\/')
		text_raw = text_raw.replace('O','0')
		text_raw = text_raw.replace('P','|*')
		text_raw = text_raw.replace('Q','(_,)')
		text_raw = text_raw.replace('R','/-')
		text_raw = text_raw.replace('S','$')
		text_raw = text_raw.replace('T','\'|\'')
		text_raw = text_raw.replace('U','|_|')
		text_raw = text_raw.replace('V','|/')
		text_raw = text_raw.replace('W','\\|/')
		text_raw = text_raw.replace('X',')(')
		text_raw = text_raw.replace('Y','`\\')
		text_raw = text_raw.replace('Z','7_')
	if leet_level == 3:
		text_raw = text_raw.replace('a','4')
		text_raw = text_raw.replace('b','8')
		text_raw = text_raw.replace('e','3')
		text_raw = text_raw.replace('g','9')
		text_raw = text_raw.replace('l','1')
		text_raw = text_raw.replace('o','0')
		text_raw = text_raw.replace('s','5')
		text_raw = text_raw.replace('t','7')
		text_raw = text_raw.replace('z','2')
		text_raw = text_raw.replace('A','/-\\')
		text_raw = text_raw.replace('B','|3')
		text_raw = text_raw.replace('C','(')
		text_raw = text_raw.replace('D','[)')
		text_raw = text_raw.replace('E','[-')
		text_raw = text_raw.replace('G','9')
		text_raw = text_raw.replace('H','|-|')
		text_raw = text_raw.replace('J','_|')
		text_raw = text_raw.replace('K','|<')
		text_raw = text_raw.replace('L','1')
		text_raw = text_raw.replace('M','|\\/|')
		text_raw = text_raw.replace('N','/\\/')
		text_raw = text_raw.replace('O','0')
		text_raw = text_raw.replace('P','|*')
		text_raw = text_raw.replace('Q','(_,)')
		text_raw = text_raw.replace('R','/-')
		text_raw = text_raw.replace('S','$')
		text_raw = text_raw.replace('T','\'|\'')
		text_raw = text_raw.replace('U','|_|')
		text_raw = text_raw.replace('V','|/')
		text_raw = text_raw.replace('W','\\|/')
		text_raw = text_raw.replace('X',')(')
		text_raw = text_raw.replace('Y','`\\')
		text_raw = text_raw.replace('Z','7_')
################################################################################################################

def lang_R_leet2():
	global text_raw, leet_level
	if leet_level == 1:
		text_raw = text_raw.replace('4','A')
		text_raw = text_raw.replace('8','B')
		text_raw = text_raw.replace('3','E')
		text_raw = text_raw.replace('9','G')
		text_raw = text_raw.replace('1','I')
		text_raw = text_raw.replace('0','O')
		text_raw = text_raw.replace('5','S')
		text_raw = text_raw.replace('7','T')
		text_raw = text_raw.replace('2','Z')
	if leet_level == 2:
		text_raw = text_raw.replace('/-\\','A')
		text_raw = text_raw.replace('|3','B')
		text_raw = text_raw.replace('9','G')
		text_raw = text_raw.replace('|-|','H')
		text_raw = text_raw.replace('|<','K')
		text_raw = text_raw.replace('|\\/|','M')
		text_raw = text_raw.replace('/\\/','N')
		text_raw = text_raw.replace('|*','P')
		text_raw = text_raw.replace('(_,)','Q')
		text_raw = text_raw.replace('/-','R')
		text_raw = text_raw.replace('$','S')
		text_raw = text_raw.replace('\'|\'','T')
		text_raw = text_raw.replace('|_|','U')
		text_raw = text_raw.replace('_|','J')
		text_raw = text_raw.replace('\\|/','W')
		text_raw = text_raw.replace('|/','V')
		text_raw = text_raw.replace('`\\','Y')
		text_raw = text_raw.replace('7_','Z')
		text_raw = text_raw.replace('[)','D')
		text_raw = text_raw.replace('[-','E')
		text_raw = text_raw.replace(')(','X')
		text_raw = text_raw.replace('(','C')
		text_raw = text_raw.replace('0','O')
	if leet_level == 3:
		text_raw = text_raw.replace('4','a')
		text_raw = text_raw.replace('8','b')
		text_raw = text_raw.replace('3','e')
		text_raw = text_raw.replace('9','g')
		text_raw = text_raw.replace('1','i')
		text_raw = text_raw.replace('0','o')
		text_raw = text_raw.replace('5','s')
		text_raw = text_raw.replace('7','t')
		text_raw = text_raw.replace('2','z')
		text_raw = text_raw.replace('/-\\','A')
		text_raw = text_raw.replace('|3','B')
		text_raw = text_raw.replace('9','G')
		text_raw = text_raw.replace('|-|','H')
		text_raw = text_raw.replace('|<','K')
		text_raw = text_raw.replace('|\\/|','M')
		text_raw = text_raw.replace('/\\/','N')
		text_raw = text_raw.replace('|*','P')
		text_raw = text_raw.replace('(_,)','Q')
		text_raw = text_raw.replace('/-','R')
		text_raw = text_raw.replace('$','S')
		text_raw = text_raw.replace('\'|\'','T')
		text_raw = text_raw.replace('|_|','U')
		text_raw = text_raw.replace('_|','J')
		text_raw = text_raw.replace('\\|/','W')
		text_raw = text_raw.replace('|/','V')
		text_raw = text_raw.replace('`\\','Y')
		text_raw = text_raw.replace('7_','Z')
		text_raw = text_raw.replace('[)','D')
		text_raw = text_raw.replace('[-','E')
		text_raw = text_raw.replace(')(','X')
		text_raw = text_raw.replace('(','C')
		text_raw = text_raw.replace('0','O')
################################################################################################################


################################################################################################################
#                                                BINARY LANGUAGE                                               #
################################################################################################################
def lang_binary():
	global text_raw
	text_raw = text_raw.replace('0',' #00#00# ')
	text_raw = text_raw.replace('1',' #00#01# ')
	text_raw = text_raw.replace(' ',' 00100000')
	text_raw = text_raw.replace('2',' #00#02# ')
	text_raw = text_raw.replace('3',' #00#03# ')
	text_raw = text_raw.replace('4',' #00#04# ')
	text_raw = text_raw.replace('5',' #00#05# ')
	text_raw = text_raw.replace('6',' #00#06# ')
	text_raw = text_raw.replace('7',' #00#07# ')
	text_raw = text_raw.replace('8',' #00#08# ')
	text_raw = text_raw.replace('9',' #00#09# ')
	text_raw = text_raw.replace('a',' 01100001')
	text_raw = text_raw.replace('b',' 01100010')
	text_raw = text_raw.replace('c',' 01100011')
	text_raw = text_raw.replace('d',' 01100100')
	text_raw = text_raw.replace('e',' 01100101')
	text_raw = text_raw.replace('f',' 01100110')
	text_raw = text_raw.replace('g',' 01100111')
	text_raw = text_raw.replace('h',' 01101000')
	text_raw = text_raw.replace('i',' 01101001')
	text_raw = text_raw.replace('j',' 01101010')
	text_raw = text_raw.replace('k',' 01101011')
	text_raw = text_raw.replace('l',' 01101100')
	text_raw = text_raw.replace('m',' 01101101')
	text_raw = text_raw.replace('n',' 01101110')
	text_raw = text_raw.replace('o',' 01101111')
	text_raw = text_raw.replace('p',' 01110000')
	text_raw = text_raw.replace('q',' 01110001')
	text_raw = text_raw.replace('r',' 01110010')
	text_raw = text_raw.replace('s',' 01110011')
	text_raw = text_raw.replace('t',' 01110100')
	text_raw = text_raw.replace('u',' 01110101')
	text_raw = text_raw.replace('v',' 01110110')
	text_raw = text_raw.replace('w',' 01110111')
	text_raw = text_raw.replace('x',' 01111000')
	text_raw = text_raw.replace('y',' 01111001')
	text_raw = text_raw.replace('z',' 01111010')
	text_raw = text_raw.replace('A',' 01000001')
	text_raw = text_raw.replace('B',' 01000010')
	text_raw = text_raw.replace('C',' 01000011')
	text_raw = text_raw.replace('D',' 01000100')
	text_raw = text_raw.replace('E',' 01000101')
	text_raw = text_raw.replace('F',' 01000110')
	text_raw = text_raw.replace('G',' 01000111')
	text_raw = text_raw.replace('H',' 01001000')
	text_raw = text_raw.replace('I',' 01001001')
	text_raw = text_raw.replace('J',' 01001010')
	text_raw = text_raw.replace('K',' 01001011')
	text_raw = text_raw.replace('L',' 01001100')
	text_raw = text_raw.replace('M',' 01001101')
	text_raw = text_raw.replace('N',' 01001110')
	text_raw = text_raw.replace('O',' 01001111')
	text_raw = text_raw.replace('P',' 01010000')
	text_raw = text_raw.replace('Q',' 01010001')
	text_raw = text_raw.replace('R',' 01010010')
	text_raw = text_raw.replace('S',' 01010011')
	text_raw = text_raw.replace('T',' 01010100')
	text_raw = text_raw.replace('U',' 01010101')
	text_raw = text_raw.replace('V',' 01010110')
	text_raw = text_raw.replace('W',' 01010111')
	text_raw = text_raw.replace('X',' 01011000')
	text_raw = text_raw.replace('Y',' 01011001')
	text_raw = text_raw.replace('Z',' 01011010')
	text_raw = text_raw.replace('!',' 00100001')
	text_raw = text_raw.replace('@',' 01000000')
	text_raw = text_raw.replace('$',' 00100100')
	text_raw = text_raw.replace('%',' 00100101')
	text_raw = text_raw.replace('^',' 01011110')
	text_raw = text_raw.replace('&',' 00100110')
	text_raw = text_raw.replace('*',' 00101010')
	text_raw = text_raw.replace('(',' 00101000')
	text_raw = text_raw.replace(')',' 00101001')
	text_raw = text_raw.replace('_',' 01011111')
	text_raw = text_raw.replace('-',' 00101101')
	text_raw = text_raw.replace('+',' 00101011')
	text_raw = text_raw.replace('=',' 00111101')
	text_raw = text_raw.replace('|',' 01111100')
	text_raw = text_raw.replace('\\',' 01011100')
	text_raw = text_raw.replace('{',' 01111011')
	text_raw = text_raw.replace('[',' 01011011')
	text_raw = text_raw.replace('}',' 01111101')
	text_raw = text_raw.replace(']',' 01011101')
	text_raw = text_raw.replace(':',' 00111010')
	text_raw = text_raw.replace(';',' 00111011')
	text_raw = text_raw.replace('"',' 00100010')
	text_raw = text_raw.replace('\'',' 00100111')
	text_raw = text_raw.replace('<',' 00111100')
	text_raw = text_raw.replace(',',' 00101100')
	text_raw = text_raw.replace('>',' 00111110')
	text_raw = text_raw.replace('.',' 00101110')
	text_raw = text_raw.replace('?',' 00111111')
	text_raw = text_raw.replace('/',' 00101111')
	text_raw = text_raw.replace(' #00#00# ','0')
	text_raw = text_raw.replace(' #00#01# ','1')
	text_raw = text_raw.replace(' #00#02# ','2')
	text_raw = text_raw.replace(' #00#03# ','3')
	text_raw = text_raw.replace(' #00#04# ','4')
	text_raw = text_raw.replace(' #00#05# ','5')
	text_raw = text_raw.replace(' #00#06# ','6')
	text_raw = text_raw.replace(' #00#07# ','7')
	text_raw = text_raw.replace(' #00#08# ','8')
	text_raw = text_raw.replace(' #00#09# ','9')
	text_raw = text_raw.replace('#',' 00100011')
	text_raw = text_raw[1:]
################################################################################################################

def lang_R_binary():
	global text_raw
	text_raw = text_raw.replace('01100001','a')
	text_raw = text_raw.replace('01100010','b')
	text_raw = text_raw.replace('01100011','c')
	text_raw = text_raw.replace('01100100','d')
	text_raw = text_raw.replace('01100101','e')
	text_raw = text_raw.replace('01100110','f')
	text_raw = text_raw.replace('01100111','g')
	text_raw = text_raw.replace('01101000','h')
	text_raw = text_raw.replace('01101001','i')
	text_raw = text_raw.replace('01101010','j')
	text_raw = text_raw.replace('01101011','k')
	text_raw = text_raw.replace('01101100','l')
	text_raw = text_raw.replace('01101101','m')
	text_raw = text_raw.replace('01101110','n')
	text_raw = text_raw.replace('01101111','o')
	text_raw = text_raw.replace('01110000','p')
	text_raw = text_raw.replace('01110001','q')
	text_raw = text_raw.replace('01110010','r')
	text_raw = text_raw.replace('01110011','s')
	text_raw = text_raw.replace('01110100','t')
	text_raw = text_raw.replace('01110101','u')
	text_raw = text_raw.replace('01110110','v')
	text_raw = text_raw.replace('01110111','w')
	text_raw = text_raw.replace('01111000','x')
	text_raw = text_raw.replace('01111001','y')
	text_raw = text_raw.replace('01111010','z')
	text_raw = text_raw.replace('01000001','A')
	text_raw = text_raw.replace('01000010','B')
	text_raw = text_raw.replace('01000011','C')
	text_raw = text_raw.replace('01000100','D')
	text_raw = text_raw.replace('01000101','E')
	text_raw = text_raw.replace('01000110','F')
	text_raw = text_raw.replace('01000111','G')
	text_raw = text_raw.replace('01001000','H')
	text_raw = text_raw.replace('01001001','I')
	text_raw = text_raw.replace('01001010','J')
	text_raw = text_raw.replace('01001011','K')
	text_raw = text_raw.replace('01001100','L')
	text_raw = text_raw.replace('01001101','M')
	text_raw = text_raw.replace('01001110','N')
	text_raw = text_raw.replace('01001111','O')
	text_raw = text_raw.replace('01010000','P')
	text_raw = text_raw.replace('01010001','Q')
	text_raw = text_raw.replace('01010010','R')
	text_raw = text_raw.replace('01010011','S')
	text_raw = text_raw.replace('01010100','T')
	text_raw = text_raw.replace('01010101','U')
	text_raw = text_raw.replace('01010110','V')
	text_raw = text_raw.replace('01010111','W')
	text_raw = text_raw.replace('01011000','X')
	text_raw = text_raw.replace('01011001','Y')
	text_raw = text_raw.replace('01011010','Z')
	text_raw = text_raw.replace('00100001','!')
	text_raw = text_raw.replace('01000000','@')
	text_raw = text_raw.replace('00100011','#')
	text_raw = text_raw.replace('00100100','$')
	text_raw = text_raw.replace('00100101','%')
	text_raw = text_raw.replace('01011110','^')
	text_raw = text_raw.replace('00100110','&')
	text_raw = text_raw.replace('00101010','*')
	text_raw = text_raw.replace('00101000','(')
	text_raw = text_raw.replace('00101001',')')
	text_raw = text_raw.replace('01011111','_')
	text_raw = text_raw.replace('00101101','-')
	text_raw = text_raw.replace('00101011','+')
	text_raw = text_raw.replace('00111101','=')
	text_raw = text_raw.replace('01111100','|')
	text_raw = text_raw.replace('01011100','\\')
	text_raw = text_raw.replace('01111011','{')
	text_raw = text_raw.replace('01011011','[')
	text_raw = text_raw.replace('01111101','}')
	text_raw = text_raw.replace('01011101',']')
	text_raw = text_raw.replace('00111010',':')
	text_raw = text_raw.replace('00111011',';')
	text_raw = text_raw.replace('00100010','"')
	text_raw = text_raw.replace('00100111','\'')
	text_raw = text_raw.replace('00111100','<')
	text_raw = text_raw.replace('00101100',',')
	text_raw = text_raw.replace('00111110','>')
	text_raw = text_raw.replace('00101110','.')
	text_raw = text_raw.replace('00111111','?')
	text_raw = text_raw.replace('00101111','/')
	text_raw = text_raw.replace('0',' #00#00# ')
	text_raw = text_raw.replace('1',' #00#01# ')
	text_raw = text_raw.replace(' ','')
	text_raw = text_raw.replace('00100000',' ')
################################################################################################################


################################################################################################################
#                                                CRAZY LANGUAGE                                                #
################################################################################################################
def lang_crazy():
	global text_raw
	text_raw = text_raw.replace('d',' #00#00# ')
	text_raw = text_raw.replace('v','d')
	text_raw = text_raw.replace('r','v')
	text_raw = text_raw.replace('b','r')
	text_raw = text_raw.replace('j','b')
	text_raw = text_raw.replace('f','j')
	text_raw = text_raw.replace('k','f')
	text_raw = text_raw.replace('l','k')
	text_raw = text_raw.replace('q','l')
	text_raw = text_raw.replace('a','q')
	text_raw = text_raw.replace('t',' #00#01# ')
	text_raw = text_raw.replace('h','t')
	text_raw = text_raw.replace('s','h')
	text_raw = text_raw.replace('c','s')
	text_raw = text_raw.replace('p','c')
	text_raw = text_raw.replace('i','p')
	text_raw = text_raw.replace('e','i')
	text_raw = text_raw.replace('g','e')
	text_raw = text_raw.replace('o','g')
	text_raw = text_raw.replace('n','o')
	text_raw = text_raw.replace('m',' #00#02# ')
	text_raw = text_raw.replace('u','m')
	text_raw = text_raw.replace('D',' #00#03# ')
	text_raw = text_raw.replace('V','D')
	text_raw = text_raw.replace('R','V')
	text_raw = text_raw.replace('B','R')
	text_raw = text_raw.replace('J','B')
	text_raw = text_raw.replace('F','J')
	text_raw = text_raw.replace('K','F')
	text_raw = text_raw.replace('L','K')
	text_raw = text_raw.replace('Q','L')
	text_raw = text_raw.replace('A','Q')
	text_raw = text_raw.replace('T',' #00#04# ')
	text_raw = text_raw.replace('H','T')
	text_raw = text_raw.replace('S','H')
	text_raw = text_raw.replace('C','S')
	text_raw = text_raw.replace('P','C')
	text_raw = text_raw.replace('I','P')
	text_raw = text_raw.replace('E','I')
	text_raw = text_raw.replace('G','E')
	text_raw = text_raw.replace('O','G')
	text_raw = text_raw.replace('N','O')
	text_raw = text_raw.replace('M',' #00#05# ')
	text_raw = text_raw.replace('U','M')
	text_raw = text_raw.replace(' #00#00# ','a')
	text_raw = text_raw.replace(' #00#01# ','n')
	text_raw = text_raw.replace(' #00#02# ','u')
	text_raw = text_raw.replace(' #00#03# ','A')
	text_raw = text_raw.replace(' #00#04# ','N')
	text_raw = text_raw.replace(' #00#05# ','U')
################################################################################################################

def lang_R_crazy():
	global text_raw
	text_raw = text_raw.replace('l',' #00#00# ')
	text_raw = text_raw.replace('k','l')
	text_raw = text_raw.replace('f','k')
	text_raw = text_raw.replace('j','f')
	text_raw = text_raw.replace('b','j')
	text_raw = text_raw.replace('r','b')
	text_raw = text_raw.replace('v','r')
	text_raw = text_raw.replace('d','v')
	text_raw = text_raw.replace('a','d')
	text_raw = text_raw.replace('q','a')
	text_raw = text_raw.replace('p',' #00#01# ')
	text_raw = text_raw.replace('c','p')
	text_raw = text_raw.replace('s','c')
	text_raw = text_raw.replace('h','s')
	text_raw = text_raw.replace('t','h')
	text_raw = text_raw.replace('n','t')
	text_raw = text_raw.replace('o','n')
	text_raw = text_raw.replace('g','o')
	text_raw = text_raw.replace('e','g')
	text_raw = text_raw.replace('i','e')
	text_raw = text_raw.replace('m',' #00#02# ')
	text_raw = text_raw.replace('u','m')
	text_raw = text_raw.replace('L',' #00#03# ')
	text_raw = text_raw.replace('K','L')
	text_raw = text_raw.replace('F','K')
	text_raw = text_raw.replace('J','F')
	text_raw = text_raw.replace('B','J')
	text_raw = text_raw.replace('R','B')
	text_raw = text_raw.replace('V','R')
	text_raw = text_raw.replace('D','V')
	text_raw = text_raw.replace('A','D')
	text_raw = text_raw.replace('Q','A')
	text_raw = text_raw.replace('P',' #00#04# ')
	text_raw = text_raw.replace('C','P')
	text_raw = text_raw.replace('S','C')
	text_raw = text_raw.replace('H','S')
	text_raw = text_raw.replace('T','H')
	text_raw = text_raw.replace('N','T')
	text_raw = text_raw.replace('O','N')
	text_raw = text_raw.replace('G','O')
	text_raw = text_raw.replace('E','G')
	text_raw = text_raw.replace('I','E')
	text_raw = text_raw.replace('M',' #00#05# ')
	text_raw = text_raw.replace('U','M')
	text_raw = text_raw.replace(' #00#00# ','q')
	text_raw = text_raw.replace(' #00#01# ','i')
	text_raw = text_raw.replace(' #00#02# ','u')
	text_raw = text_raw.replace(' #00#03# ','Q')
	text_raw = text_raw.replace(' #00#04# ','I')
	text_raw = text_raw.replace(' #00#05# ','U')
################################################################################################################


################################################################################################################
#                                               CRAZY LANGUAGE 2                                               #
################################################################################################################
def lang_crazy2():
	global text_raw
	text_raw = text_raw.replace('c',' #00#00# ')
	text_raw = text_raw.replace('l','c')
	text_raw = text_raw.replace('k','l')
	text_raw = text_raw.replace('j','k')
	text_raw = text_raw.replace('e','j')
	text_raw = text_raw.replace('g','e')
	text_raw = text_raw.replace('m','g')
	text_raw = text_raw.replace('n','m')
	text_raw = text_raw.replace('o','n')
	text_raw = text_raw.replace('r','o')
	text_raw = text_raw.replace('w','r')
	text_raw = text_raw.replace('q','w')
	text_raw = text_raw.replace('v','q')
	text_raw = text_raw.replace('p','v')
	text_raw = text_raw.replace('s','p')
	text_raw = text_raw.replace('a','s')
	text_raw = text_raw.replace('b','a')
	text_raw = text_raw.replace('u',' #00#01# ')
	text_raw = text_raw.replace('i','u')
	text_raw = text_raw.replace('d','i')
	text_raw = text_raw.replace('h',' #00#02# ')
	text_raw = text_raw.replace('t','h')
	text_raw = text_raw.replace('C',' #00#03# ')
	text_raw = text_raw.replace('L','C')
	text_raw = text_raw.replace('K','L')
	text_raw = text_raw.replace('J','K')
	text_raw = text_raw.replace('E','J')
	text_raw = text_raw.replace('G','E')
	text_raw = text_raw.replace('M','G')
	text_raw = text_raw.replace('N','M')
	text_raw = text_raw.replace('O','N')
	text_raw = text_raw.replace('R','O')
	text_raw = text_raw.replace('W','R')
	text_raw = text_raw.replace('Q','W')
	text_raw = text_raw.replace('V','Q')
	text_raw = text_raw.replace('P','V')
	text_raw = text_raw.replace('S','P')
	text_raw = text_raw.replace('A','S')
	text_raw = text_raw.replace('B','A')
	text_raw = text_raw.replace('U',' #00#04# ')
	text_raw = text_raw.replace('I','U')
	text_raw = text_raw.replace('D','I')
	text_raw = text_raw.replace('H',' #00#05# ')
	text_raw = text_raw.replace('T','H')
	text_raw = text_raw.replace(' #00#00# ','b')
	text_raw = text_raw.replace(' #00#01# ','d')
	text_raw = text_raw.replace(' #00#02# ','t')
	text_raw = text_raw.replace(' #00#03# ','B')
	text_raw = text_raw.replace(' #00#04# ','D')
	text_raw = text_raw.replace(' #00#05# ','T')
################################################################################################################

def lang_R_crazy2():
	global text_raw
	text_raw = text_raw.replace('k',' #00#00# ')
	text_raw = text_raw.replace('l','k')
	text_raw = text_raw.replace('c','l')
	text_raw = text_raw.replace('b','c')
	text_raw = text_raw.replace('a','b')
	text_raw = text_raw.replace('s','a')
	text_raw = text_raw.replace('u',' #00#01# ')
	text_raw = text_raw.replace('d','u')
	text_raw = text_raw.replace('i','d')
	text_raw = text_raw.replace('e',' #00#02# ')
	text_raw = text_raw.replace('j','e')
	text_raw = text_raw.replace('h',' #00#03# ')
	text_raw = text_raw.replace('t','h')
	text_raw = text_raw.replace('p','s')
	text_raw = text_raw.replace('v','p')
	text_raw = text_raw.replace('q','v')
	text_raw = text_raw.replace('w','q')
	text_raw = text_raw.replace('r','w')
	text_raw = text_raw.replace('o','r')
	text_raw = text_raw.replace('n','o')
	text_raw = text_raw.replace('m','n')
	text_raw = text_raw.replace('g','m')
	text_raw = text_raw.replace('K',' #00#04# ')
	text_raw = text_raw.replace('L','K')
	text_raw = text_raw.replace('C','L')
	text_raw = text_raw.replace('B','C')
	text_raw = text_raw.replace('A','B')
	text_raw = text_raw.replace('S','A')
	text_raw = text_raw.replace('U',' #00#05# ')
	text_raw = text_raw.replace('D','U')
	text_raw = text_raw.replace('I','D')
	text_raw = text_raw.replace('E',' #00#06# ')
	text_raw = text_raw.replace('J','E')
	text_raw = text_raw.replace('H',' #00#07# ')
	text_raw = text_raw.replace('T','H')
	text_raw = text_raw.replace('P','S')
	text_raw = text_raw.replace('V','P')
	text_raw = text_raw.replace('Q','V')
	text_raw = text_raw.replace('W','Q')
	text_raw = text_raw.replace('R','W')
	text_raw = text_raw.replace('O','R')
	text_raw = text_raw.replace('N','O')
	text_raw = text_raw.replace('M','N')
	text_raw = text_raw.replace('G','M')
	text_raw = text_raw.replace(' #00#00# ','j')
	text_raw = text_raw.replace(' #00#01# ','i')
	text_raw = text_raw.replace(' #00#02# ','g')
	text_raw = text_raw.replace(' #00#03# ','t')
	text_raw = text_raw.replace(' #00#04# ','J')
	text_raw = text_raw.replace(' #00#05# ','I')
	text_raw = text_raw.replace(' #00#06# ','G')
	text_raw = text_raw.replace(' #00#07# ','T')
################################################################################################################


################################################################################################################
#                                              BACKWARDS ALPHABET                                              #
################################################################################################################
def lang_backwards():
	global text_raw
	text_raw = text_raw.replace('a',' #00#00# ')
	text_raw = text_raw.replace('b',' #00#01# ')
	text_raw = text_raw.replace('c',' #00#02# ')
	text_raw = text_raw.replace('d',' #00#03# ')
	text_raw = text_raw.replace('e',' #00#04# ')
	text_raw = text_raw.replace('f',' #00#05# ')
	text_raw = text_raw.replace('g',' #00#06# ')
	text_raw = text_raw.replace('h',' #00#07# ')
	text_raw = text_raw.replace('i',' #00#08# ')
	text_raw = text_raw.replace('j',' #00#09# ')
	text_raw = text_raw.replace('k',' #00#10# ')
	text_raw = text_raw.replace('l',' #00#11# ')
	text_raw = text_raw.replace('m',' #00#13# ')
	text_raw = text_raw.replace('n','m')
	text_raw = text_raw.replace('o','l')
	text_raw = text_raw.replace('p','k')
	text_raw = text_raw.replace('q','j')
	text_raw = text_raw.replace('r','i')
	text_raw = text_raw.replace('s','h')
	text_raw = text_raw.replace('t','g')
	text_raw = text_raw.replace('u','f')
	text_raw = text_raw.replace('v','e')
	text_raw = text_raw.replace('w','d')
	text_raw = text_raw.replace('x','c')
	text_raw = text_raw.replace('y','b')
	text_raw = text_raw.replace('z','a')
	text_raw = text_raw.replace('A',' #00#14# ')
	text_raw = text_raw.replace('B',' #00#15# ')
	text_raw = text_raw.replace('C',' #00#16# ')
	text_raw = text_raw.replace('D',' #00#17# ')
	text_raw = text_raw.replace('E',' #00#18# ')
	text_raw = text_raw.replace('F',' #00#19# ')
	text_raw = text_raw.replace('G',' #00#20# ')
	text_raw = text_raw.replace('H',' #00#21# ')
	text_raw = text_raw.replace('I',' #00#22# ')
	text_raw = text_raw.replace('J',' #00#23# ')
	text_raw = text_raw.replace('K',' #00#24# ')
	text_raw = text_raw.replace('L',' #00#25# ')
	text_raw = text_raw.replace('M',' #00#26# ')
	text_raw = text_raw.replace('N','M')
	text_raw = text_raw.replace('O','L')
	text_raw = text_raw.replace('P','K')
	text_raw = text_raw.replace('Q','J')
	text_raw = text_raw.replace('R','I')
	text_raw = text_raw.replace('S','H')
	text_raw = text_raw.replace('T','G')
	text_raw = text_raw.replace('U','F')
	text_raw = text_raw.replace('V','E')
	text_raw = text_raw.replace('W','D')
	text_raw = text_raw.replace('X','C')
	text_raw = text_raw.replace('Y','B')
	text_raw = text_raw.replace('Z','A')
	text_raw = text_raw.replace(' #00#00# ','z')
	text_raw = text_raw.replace(' #00#01# ','y')
	text_raw = text_raw.replace(' #00#02# ','x')
	text_raw = text_raw.replace(' #00#03# ','w')
	text_raw = text_raw.replace(' #00#04# ','v')
	text_raw = text_raw.replace(' #00#05# ','u')
	text_raw = text_raw.replace(' #00#06# ','t')
	text_raw = text_raw.replace(' #00#07# ','s')
	text_raw = text_raw.replace(' #00#08# ','r')
	text_raw = text_raw.replace(' #00#09# ','q')
	text_raw = text_raw.replace(' #00#10# ','p')
	text_raw = text_raw.replace(' #00#11# ','o')
	text_raw = text_raw.replace(' #00#13# ','n')
	text_raw = text_raw.replace(' #00#14# ','Z')
	text_raw = text_raw.replace(' #00#15# ','Y')
	text_raw = text_raw.replace(' #00#16# ','X')
	text_raw = text_raw.replace(' #00#17# ','W')
	text_raw = text_raw.replace(' #00#18# ','V')
	text_raw = text_raw.replace(' #00#19# ','U')
	text_raw = text_raw.replace(' #00#20# ','T')
	text_raw = text_raw.replace(' #00#21# ','S')
	text_raw = text_raw.replace(' #00#22# ','R')
	text_raw = text_raw.replace(' #00#23# ','Q')
	text_raw = text_raw.replace(' #00#24# ','P')
	text_raw = text_raw.replace(' #00#25# ','O')
	text_raw = text_raw.replace(' #00#26# ','N')
################################################################################################################


################################################################################################################
#                                             LANGS - 3R/2R/1R + 3L/2L/1L                                            #
################################################################################################################
def lang_3R():
	global text_raw
	text_raw = text_raw.replace('s',' #00#00# ')
	text_raw = text_raw.replace('v','s')
	text_raw = text_raw.replace('y','v')
	text_raw = text_raw.replace('b','y')
	text_raw = text_raw.replace('e','b')
	text_raw = text_raw.replace('h','e')
	text_raw = text_raw.replace('k','h')
	text_raw = text_raw.replace('n','k')
	text_raw = text_raw.replace('q','n')
	text_raw = text_raw.replace('t','q')
	text_raw = text_raw.replace('w','t')
	text_raw = text_raw.replace('z','w')
	text_raw = text_raw.replace('c','z')
	text_raw = text_raw.replace('f','c')
	text_raw = text_raw.replace('i','f')
	text_raw = text_raw.replace('l','i')
	text_raw = text_raw.replace('o','l')
	text_raw = text_raw.replace('r','o')
	text_raw = text_raw.replace('u','r')
	text_raw = text_raw.replace('x','u')
	text_raw = text_raw.replace('a','x')
	text_raw = text_raw.replace('d','a')
	text_raw = text_raw.replace('g','d')
	text_raw = text_raw.replace('j','g')
	text_raw = text_raw.replace('m','j')
	text_raw = text_raw.replace('p','m')
	text_raw = text_raw.replace('S',' #00#00# ')
	text_raw = text_raw.replace('V','S')
	text_raw = text_raw.replace('Y','V')
	text_raw = text_raw.replace('B','Y')
	text_raw = text_raw.replace('E','B')
	text_raw = text_raw.replace('H','E')
	text_raw = text_raw.replace('K','H')
	text_raw = text_raw.replace('N','K')
	text_raw = text_raw.replace('Q','N')
	text_raw = text_raw.replace('T','Q')
	text_raw = text_raw.replace('W','T')
	text_raw = text_raw.replace('Z','W')
	text_raw = text_raw.replace('C','Z')
	text_raw = text_raw.replace('F','C')
	text_raw = text_raw.replace('I','F')
	text_raw = text_raw.replace('L','I')
	text_raw = text_raw.replace('O','L')
	text_raw = text_raw.replace('R','O')
	text_raw = text_raw.replace('U','R')
	text_raw = text_raw.replace('X','U')
	text_raw = text_raw.replace('A','X')
	text_raw = text_raw.replace('D','A')
	text_raw = text_raw.replace('G','D')
	text_raw = text_raw.replace('J','G')
	text_raw = text_raw.replace('M','J')
	text_raw = text_raw.replace('P','M')
	text_raw = text_raw.replace(' #00#00# ','p')
	text_raw = text_raw.replace(' #00#01# ','P')
################################################################################################################


def lang_3L():
	global text_raw
	text_raw = text_raw.replace('x',' #00#00# ')
	text_raw = text_raw.replace('u','x')
	text_raw = text_raw.replace('r','u')
	text_raw = text_raw.replace('o','r')
	text_raw = text_raw.replace('l','o')
	text_raw = text_raw.replace('i','l')
	text_raw = text_raw.replace('f','i')
	text_raw = text_raw.replace('c','f')
	text_raw = text_raw.replace('z','c')
	text_raw = text_raw.replace('w','z')
	text_raw = text_raw.replace('t','w')
	text_raw = text_raw.replace('q','t')
	text_raw = text_raw.replace('n','q')
	text_raw = text_raw.replace('k','n')
	text_raw = text_raw.replace('h','k')
	text_raw = text_raw.replace('e','h')
	text_raw = text_raw.replace('b','e')
	text_raw = text_raw.replace('y','b')
	text_raw = text_raw.replace('v','y')
	text_raw = text_raw.replace('s','v')
	text_raw = text_raw.replace('p','s')
	text_raw = text_raw.replace('m','p')
	text_raw = text_raw.replace('j','m')
	text_raw = text_raw.replace('g','j')
	text_raw = text_raw.replace('d','g')
	text_raw = text_raw.replace('a','d')
	text_raw = text_raw.replace('X',' #00#01# ')
	text_raw = text_raw.replace('U','X')
	text_raw = text_raw.replace('R','U')
	text_raw = text_raw.replace('O','R')
	text_raw = text_raw.replace('L','O')
	text_raw = text_raw.replace('I','L')
	text_raw = text_raw.replace('F','I')
	text_raw = text_raw.replace('C','F')
	text_raw = text_raw.replace('Z','C')
	text_raw = text_raw.replace('W','Z')
	text_raw = text_raw.replace('T','W')
	text_raw = text_raw.replace('Q','T')
	text_raw = text_raw.replace('N','Q')
	text_raw = text_raw.replace('K','N')
	text_raw = text_raw.replace('H','K')
	text_raw = text_raw.replace('E','H')
	text_raw = text_raw.replace('B','E')
	text_raw = text_raw.replace('Y','B')
	text_raw = text_raw.replace('V','Y')
	text_raw = text_raw.replace('S','V')
	text_raw = text_raw.replace('P','S')
	text_raw = text_raw.replace('M','P')
	text_raw = text_raw.replace('J','M')
	text_raw = text_raw.replace('G','J')
	text_raw = text_raw.replace('D','G')
	text_raw = text_raw.replace('A','D')
	text_raw = text_raw.replace(' #00#00# ','a')
	text_raw = text_raw.replace(' #00#01# ','A')
################################################################################################################


def lang_2R():
	global text_raw
	text_raw = text_raw.replace('c',' #00#00# ')
	text_raw = text_raw.replace('e','c')
	text_raw = text_raw.replace('g','e')
	text_raw = text_raw.replace('i','g')
	text_raw = text_raw.replace('k','i')
	text_raw = text_raw.replace('m','k')
	text_raw = text_raw.replace('o','m')
	text_raw = text_raw.replace('q','o')
	text_raw = text_raw.replace('s','q')
	text_raw = text_raw.replace('u','s')
	text_raw = text_raw.replace('w','u')
	text_raw = text_raw.replace('y','w')
	text_raw = text_raw.replace('a','y')
	text_raw = text_raw.replace('b',' #00#01# ')
	text_raw = text_raw.replace('d','b')
	text_raw = text_raw.replace('f','d')
	text_raw = text_raw.replace('h','f')
	text_raw = text_raw.replace('j','h')
	text_raw = text_raw.replace('l','j')
	text_raw = text_raw.replace('n','l')
	text_raw = text_raw.replace('p','n')
	text_raw = text_raw.replace('r','p')
	text_raw = text_raw.replace('t','r')
	text_raw = text_raw.replace('v','t')
	text_raw = text_raw.replace('x','v')
	text_raw = text_raw.replace('z','x')
	text_raw = text_raw.replace('C',' #00#02# ')
	text_raw = text_raw.replace('E','C')
	text_raw = text_raw.replace('G','E')
	text_raw = text_raw.replace('I','G')
	text_raw = text_raw.replace('K','I')
	text_raw = text_raw.replace('M','K')
	text_raw = text_raw.replace('O',',')
	text_raw = text_raw.replace('Q','O')
	text_raw = text_raw.replace('S','Q')
	text_raw = text_raw.replace('U','S')
	text_raw = text_raw.replace('W','U')
	text_raw = text_raw.replace('Y','W')
	text_raw = text_raw.replace('A','Y')
	text_raw = text_raw.replace('B',' #00#03# ')
	text_raw = text_raw.replace('D','B')
	text_raw = text_raw.replace('F','D')
	text_raw = text_raw.replace('H','F')
	text_raw = text_raw.replace('J','H')
	text_raw = text_raw.replace('L','J')
	text_raw = text_raw.replace('N','L')
	text_raw = text_raw.replace('P','N')
	text_raw = text_raw.replace('R','P')
	text_raw = text_raw.replace('T','R')
	text_raw = text_raw.replace('V','T')
	text_raw = text_raw.replace('X','V')
	text_raw = text_raw.replace('Z','X')
	text_raw = text_raw.replace(' #00#00# ','a')
	text_raw = text_raw.replace(' #00#01# ','z')
	text_raw = text_raw.replace(' #00#02# ','A')
	text_raw = text_raw.replace(' #00#03# ','Z')
################################################################################################################


def lang_2L():
	global text_raw
	text_raw = text_raw.replace('y',' #00#00# ')
	text_raw = text_raw.replace('w','y')
	text_raw = text_raw.replace('u','w')
	text_raw = text_raw.replace('s','u')
	text_raw = text_raw.replace('q','s')
	text_raw = text_raw.replace('o','q')
	text_raw = text_raw.replace('m','o')
	text_raw = text_raw.replace('k','m')
	text_raw = text_raw.replace('i','k')
	text_raw = text_raw.replace('g','i')
	text_raw = text_raw.replace('e','g')
	text_raw = text_raw.replace('c','e')
	text_raw = text_raw.replace('a','c')
	text_raw = text_raw.replace('d',' #00#01# ')
	text_raw = text_raw.replace('b','d')
	text_raw = text_raw.replace('h',' #00#02# ')
	text_raw = text_raw.replace('f','h')
	text_raw = text_raw.replace('l',' #00#03# ')
	text_raw = text_raw.replace('j','l')
	text_raw = text_raw.replace('p',' #00#04# ')
	text_raw = text_raw.replace('n','p')
	text_raw = text_raw.replace('t',' #00#05# ')
	text_raw = text_raw.replace('r','t')
	text_raw = text_raw.replace('x',' #00#06# ')
	text_raw = text_raw.replace('v','x')
	text_raw = text_raw.replace('z','b')
	text_raw = text_raw.replace('Y',' #00#07# ')
	text_raw = text_raw.replace('W','Y')
	text_raw = text_raw.replace('U','W')
	text_raw = text_raw.replace('S','U')
	text_raw = text_raw.replace('Q','S')
	text_raw = text_raw.replace('O','Q')
	text_raw = text_raw.replace('M','O')
	text_raw = text_raw.replace('K','M')
	text_raw = text_raw.replace('I','K')
	text_raw = text_raw.replace('G','I')
	text_raw = text_raw.replace('E','G')
	text_raw = text_raw.replace('C','E')
	text_raw = text_raw.replace('A','C')
	text_raw = text_raw.replace('D',' #00#08# ')
	text_raw = text_raw.replace('B','D')
	text_raw = text_raw.replace('H',' #00#09# ')
	text_raw = text_raw.replace('F','H')
	text_raw = text_raw.replace('L',' #00#10# ')
	text_raw = text_raw.replace('J','L')
	text_raw = text_raw.replace('P',' #00#11#')
	text_raw = text_raw.replace('N','P')
	text_raw = text_raw.replace('T',' #00#13# ')
	text_raw = text_raw.replace('R','T')
	text_raw = text_raw.replace('X',' #00#14# ')
	text_raw = text_raw.replace('V','X')
	text_raw = text_raw.replace('Z','B')
	text_raw = text_raw.replace(' #00#00# ','a')
	text_raw = text_raw.replace(' #00#01# ','f')
	text_raw = text_raw.replace(' #00#02# ','j')
	text_raw = text_raw.replace(' #00#03# ','n')
	text_raw = text_raw.replace(' #00#04# ','r')
	text_raw = text_raw.replace(' #00#05# ','v')
	text_raw = text_raw.replace(' #00#06# ','z')
	text_raw = text_raw.replace(' #00#07# ','A')
	text_raw = text_raw.replace(' #00#08# ','F')
	text_raw = text_raw.replace(' #00#09# ','J')
	text_raw = text_raw.replace(' #00#10# ','N')
	text_raw = text_raw.replace(' #00#11# ','R')
	text_raw = text_raw.replace(' #00#13# ','V')
	text_raw = text_raw.replace(' #00#14# ','Z')
################################################################################################################


def lang_1R():
	global text_raw
	text_raw = text_raw.replace('b',' #00#00# ')
	text_raw = text_raw.replace('c','b')
	text_raw = text_raw.replace('d','c')
	text_raw = text_raw.replace('e','d')
	text_raw = text_raw.replace('f','e')
	text_raw = text_raw.replace('g','f')
	text_raw = text_raw.replace('h','g')
	text_raw = text_raw.replace('i','h')
	text_raw = text_raw.replace('j','i')
	text_raw = text_raw.replace('k','j')
	text_raw = text_raw.replace('l','k')
	text_raw = text_raw.replace('m','l')
	text_raw = text_raw.replace('n','m')
	text_raw = text_raw.replace('o','n')
	text_raw = text_raw.replace('p','o')
	text_raw = text_raw.replace('q','p')
	text_raw = text_raw.replace('r','q')
	text_raw = text_raw.replace('s','r')
	text_raw = text_raw.replace('t','s')
	text_raw = text_raw.replace('u','t')
	text_raw = text_raw.replace('v','u')
	text_raw = text_raw.replace('w','v')
	text_raw = text_raw.replace('x','w')
	text_raw = text_raw.replace('y','x')
	text_raw = text_raw.replace('z','y')
	text_raw = text_raw.replace('a','z')
	text_raw = text_raw.replace('B',' #00#01# ')
	text_raw = text_raw.replace('C','B')
	text_raw = text_raw.replace('D','C')
	text_raw = text_raw.replace('E','D')
	text_raw = text_raw.replace('F','E')
	text_raw = text_raw.replace('G','F')
	text_raw = text_raw.replace('H','G')
	text_raw = text_raw.replace('I','H')
	text_raw = text_raw.replace('J','I')
	text_raw = text_raw.replace('K','J')
	text_raw = text_raw.replace('L','K')
	text_raw = text_raw.replace('M','L')
	text_raw = text_raw.replace('N','M')
	text_raw = text_raw.replace('O','N')
	text_raw = text_raw.replace('P','O')
	text_raw = text_raw.replace('Q','P')
	text_raw = text_raw.replace('R','Q')
	text_raw = text_raw.replace('S','R')
	text_raw = text_raw.replace('T','S')
	text_raw = text_raw.replace('U','T')
	text_raw = text_raw.replace('V','U')
	text_raw = text_raw.replace('W','V')
	text_raw = text_raw.replace('X','W')
	text_raw = text_raw.replace('Y','X')
	text_raw = text_raw.replace('Z','Y')
	text_raw = text_raw.replace('A','Z')
	text_raw = text_raw.replace(' #00#00# ','a')
	text_raw = text_raw.replace(' #00#01# ','A')
################################################################################################################


def lang_1L():
	global text_raw
	text_raw = text_raw.replace('z',' #00#00# ')
	text_raw = text_raw.replace('y','z')
	text_raw = text_raw.replace('x','y')
	text_raw = text_raw.replace('w','x')
	text_raw = text_raw.replace('v','w')
	text_raw = text_raw.replace('u','v')
	text_raw = text_raw.replace('t','u')
	text_raw = text_raw.replace('s','t')
	text_raw = text_raw.replace('r','s')
	text_raw = text_raw.replace('q','r')
	text_raw = text_raw.replace('p','q')
	text_raw = text_raw.replace('o','p')
	text_raw = text_raw.replace('n','o')
	text_raw = text_raw.replace('m','n')
	text_raw = text_raw.replace('l','m')
	text_raw = text_raw.replace('k','l')
	text_raw = text_raw.replace('j','k')
	text_raw = text_raw.replace('i','j')
	text_raw = text_raw.replace('h','i')
	text_raw = text_raw.replace('g','h')
	text_raw = text_raw.replace('f','g')
	text_raw = text_raw.replace('e','f')
	text_raw = text_raw.replace('d','e')
	text_raw = text_raw.replace('c','d')
	text_raw = text_raw.replace('b','c')
	text_raw = text_raw.replace('a','b')
	text_raw = text_raw.replace('Z',' #00#00# ')
	text_raw = text_raw.replace('Y','Z')
	text_raw = text_raw.replace('X','Y')
	text_raw = text_raw.replace('W','X')
	text_raw = text_raw.replace('V','W')
	text_raw = text_raw.replace('U','V')
	text_raw = text_raw.replace('T','U')
	text_raw = text_raw.replace('S','T')
	text_raw = text_raw.replace('R','S')
	text_raw = text_raw.replace('Q','R')
	text_raw = text_raw.replace('P','Q')
	text_raw = text_raw.replace('O','P')
	text_raw = text_raw.replace('N','O')
	text_raw = text_raw.replace('M','N')
	text_raw = text_raw.replace('L','M')
	text_raw = text_raw.replace('K','L')
	text_raw = text_raw.replace('J','K')
	text_raw = text_raw.replace('I','J')
	text_raw = text_raw.replace('H','I')
	text_raw = text_raw.replace('G','H')
	text_raw = text_raw.replace('F','G')
	text_raw = text_raw.replace('E','F')
	text_raw = text_raw.replace('D','E')
	text_raw = text_raw.replace('C','D')
	text_raw = text_raw.replace('B','C')
	text_raw = text_raw.replace('A','B')
	text_raw = text_raw.replace(' #00#00# ','a')
	text_raw = text_raw.replace(' #00#01# ','A')
################################################################################################################


################################################################################################################
#                                             UPPERCASE / LOWERCASE                                            #
################################################################################################################
def lang_LC():
	global text_raw
	text_raw = text_raw.replace('a','A')
	text_raw = text_raw.replace('b','B')
	text_raw = text_raw.replace('c','C')
	text_raw = text_raw.replace('d','D')
	text_raw = text_raw.replace('e','E')
	text_raw = text_raw.replace('f','F')
	text_raw = text_raw.replace('g','G')
	text_raw = text_raw.replace('h','H')
	text_raw = text_raw.replace('i','I')
	text_raw = text_raw.replace('j','J')
	text_raw = text_raw.replace('k','K')
	text_raw = text_raw.replace('l','L')
	text_raw = text_raw.replace('m','M')
	text_raw = text_raw.replace('n','N')
	text_raw = text_raw.replace('o','O')
	text_raw = text_raw.replace('p','P')
	text_raw = text_raw.replace('q','Q')
	text_raw = text_raw.replace('r','R')
	text_raw = text_raw.replace('s','S')
	text_raw = text_raw.replace('t','T')
	text_raw = text_raw.replace('u','U')
	text_raw = text_raw.replace('v','V')
	text_raw = text_raw.replace('w','W')
	text_raw = text_raw.replace('x','X')
	text_raw = text_raw.replace('y','Y')
	text_raw = text_raw.replace('z','Z')


def lang_UC():
	global text_raw
	text_raw = text_raw.replace('A','a')
	text_raw = text_raw.replace('B','b')
	text_raw = text_raw.replace('C','c')
	text_raw = text_raw.replace('D','d')
	text_raw = text_raw.replace('E','e')
	text_raw = text_raw.replace('F','f')
	text_raw = text_raw.replace('G','g')
	text_raw = text_raw.replace('H','h')
	text_raw = text_raw.replace('I','i')
	text_raw = text_raw.replace('J','j')
	text_raw = text_raw.replace('K','k')
	text_raw = text_raw.replace('L','l')
	text_raw = text_raw.replace('M','m')
	text_raw = text_raw.replace('N','n')
	text_raw = text_raw.replace('O','o')
	text_raw = text_raw.replace('P','p')
	text_raw = text_raw.replace('Q','q')
	text_raw = text_raw.replace('R','r')
	text_raw = text_raw.replace('S','s')
	text_raw = text_raw.replace('T','t')
	text_raw = text_raw.replace('U','u')
	text_raw = text_raw.replace('V','v')
	text_raw = text_raw.replace('W','w')
	text_raw = text_raw.replace('X','x')
	text_raw = text_raw.replace('Y','y')
	text_raw = text_raw.replace('Z','z')
################################################################################################################


################################################################################################################
#                                 VOWEL REPLACER - CHOOSE METHOD: Easy/Advanced                                #
################################################################################################################
def lang_VR():
	global text_raw, VR_EoA, VR_UseUoL, VR_UseY, VR_A_a_Equals, VR_A_e_Equals, VR_A_i_Equals, VR_A_o_Equals, VR_A_u_Equals, VR_A_y_Equals, VR_A_A_Equals, VR_A_E_Equals, VR_A_I_Equals, VR_A_O_Equals, VR_A_U_Equals, VR_A_Y_Equals
	os.system('title Vowel Replacer && cls')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	print('              \033[1;36m╔═══════════════\033[1;31m══════════════╗')
	print('              \033[1;36m║         VOWEL \033[1;31mREPLACER      ║')
	print('              \033[1;36m╠═══════════════\033[1;31m══════════════╣')
	print('              \033[1;36m║  1. Choose Easy / Advanced  \033[1;31m║')
	print('              \033[1;36m║  2. Choose Upper/Lowercase  \033[1;31m║')
	print('              \033[1;36m║ 3. Choose which "y"s to use \033[1;31m║')
	print('              \033[1;36m║      ╔═════════\033[1;31m═══════╗     ║')
	print('              \033[1;36m╚══════╣     \033[1;37m1. \033[1;36mEasy    \033[1;31m╠═════╝')
	print('                     \033[1;36m║   \033[1;37m2. \033[1;31mAdvanced  ║')
	print('                     \033[1;36m╚═════════\033[1;31m═══════╝')
	print('\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=\033[1;36m=\033[1;31m=')
	VR_EoA = input('\033[1;36mChoose an option: \033[1;33m').lower() #VowelReplacer_EasyorAdvanced
	if VR_EoA == '1' or VR_EoA == '2':
		pass
	elif VR_EoA == 'b':
		Main()
	else:
		lang_VR()
################################################################################################################
#                            ASK IF THEY WANT TO INCLUDE UPPERCASE/LOWERCASE LETTERS                           #
################################################################################################################
	def F_VR_UseUoL(): # Function_VowelReplacer_UseUppercaseOrLowercase
		global VR_UseUoL
		os.system('cls')
		print('	\033[1;36m╔══════════════════════\033[1;31m═════════════════════════╗')
		print('	\033[1;36m║           UPPERCASE o\033[1;31mr LOWERCASE              ║')
		print('	\033[1;36m╚══════════════════════\033[1;31m═════════════════════════╝')
		VR_UseUoL = input('\n\033[1;37m1. \033[1;36mLOWERCASE\n\033[1;37m2. \033[1;36mUPPERCASE\n\033[1;37m3. \033[1;36mLOWERCASE + UPPERCASE\n\n\033[1;36mChoose an option: \033[1;33m').lower()
		if VR_UseUoL == '1' or VR_UseUoL == '2' or VR_UseUoL == '3':
			pass
		elif VR_UseUoL == '' or VR_UseUoL == 'b':
			Main()
		else:
			F_VR_UseUoL()
	F_VR_UseUoL()
################################################################################################################
#                              ASK IF THEY WANT TO INCLUDE UPPERCASE/LOWERCASE Y's                             #
################################################################################################################
	def F_VR_UseY(): # Function_VowelReplacer_UseY
		global VR_UseY, VR_E_RW
		os.system('cls')
		print('	\033[1;36m╔══════════════════════\033[1;31m═════════════════════════╗')
		print('	\033[1;36m║       USE UPPERCASE o\033[1;31mr LOWERCASE "Y\'s"        ║')
		print('	\033[1;36m╚══════════════════════\033[1;31m═════════════════════════╝')
		VR_UseY = input('\n\033[1;37m1. \033[1;36mInclude only "y"\n\033[1;37m2. \033[1;36mInclude only "Y"\n\033[1;37m3. \033[1;36mInclude "y" and "Y"\n\n\033[1;37mChoose an option: \033[1;33m').lower()
		if VR_UseY == '1' or VR_UseY == '2' or VR_UseY == '3':
			pass
		elif VR_UseY == '' or VR_UseY == 'b':
			Main()
		else:
			F_VR_UseY()
	F_VR_UseY()


################################################################################################################
#                                               CHANGE VOWELS TO                                               #
################################################################################################################
	if VR_EoA == '1':
		VR_E_RW = input('\n\033[1;36mReplace all vowels with what?: \033[1;33m') #VowelReplacer_Easy_ReplaceWith
	if VR_EoA == '2':
		VR_A_a_Equals = input('\n\033[1;36ma = \033[1;33m')
		VR_A_e_Equals = input('\033[1;36me = \033[1;33m')
		VR_A_i_Equals = input('\033[1;36mi = \033[1;33m')
		VR_A_o_Equals = input('\033[1;36mo = \033[1;33m')
		VR_A_u_Equals = input('\033[1;36mu = \033[1;33m')
		if VR_UseY == '1' or VR_UseY == '3':
			VR_A_y_Equals = input('\033[1;36my = \033[1;33m')
		VR_A_A_Equals = input('\n\033[1;36mA = \033[1;33m')
		VR_A_E_Equals = input('\033[1;36mE = \033[1;33m')
		VR_A_I_Equals = input('\033[1;36mI = \033[1;33m')
		VR_A_O_Equals = input('\033[1;36mO = \033[1;33m')
		VR_A_U_Equals = input('\033[1;36mU = \033[1;33m')
		if VR_UseY == '2' or VR_UseY == '3':
			VR_A_Y_Equals = input('\033[1;36mY = \033[1;33m')
	if MT_VR_ALR_PASSED == 0:
		T2E()
################################################################################################################
#                                               START ENCRYPTING                                               #
################################################################################################################
	if VR_EoA == '1':
		text_raw = text_raw.replace('a',VR_E_RW)
		text_raw = text_raw.replace('e',VR_E_RW)
		text_raw = text_raw.replace('i',VR_E_RW)
		text_raw = text_raw.replace('o',VR_E_RW)
		text_raw = text_raw.replace('u',VR_E_RW)
		if VR_UseY == '1' or VR_UseY == '3':
			text_raw = text_raw.replace('y',VR_E_RW)
		text_raw = text_raw.replace('A',VR_E_RW)
		text_raw = text_raw.replace('E',VR_E_RW)
		text_raw = text_raw.replace('I',VR_E_RW)
		text_raw = text_raw.replace('O',VR_E_RW)
		text_raw = text_raw.replace('U',VR_E_RW)
		if VR_UseY == '2' or VR_UseY == '3':
			text_raw = text_raw.replace('Y',VR_E_RW)

	if VR_EoA == '2':
		text_raw = text_raw.replace('a',VR_A_a_Equals)
		text_raw = text_raw.replace('e',VR_A_e_Equals)
		text_raw = text_raw.replace('i',VR_A_i_Equals)
		text_raw = text_raw.replace('o',VR_A_o_Equals)
		text_raw = text_raw.replace('u',VR_A_u_Equals)
		if VR_UseY == '1' or VR_UseY == '3':
			text_raw = text_raw.replace('y',VR_A_y_Equals)
		text_raw = text_raw.replace('A',VR_A_A_Equals)
		text_raw = text_raw.replace('E',VR_A_E_Equals)
		text_raw = text_raw.replace('I',VR_A_I_Equals)
		text_raw = text_raw.replace('O',VR_A_O_Equals)
		text_raw = text_raw.replace('U',VR_A_U_Equals)
		if VR_UseY == '2' or VR_UseY == '3':
			text_raw = text_raw.replace('Y',VR_A_Y_Equals)
################################################################################################################


################################################################################################################
#                                TEXT FOR WHEN THE USER INPUTS A INVALID OPTION                                #
################################################################################################################
def INV_OPT():
	print('                     \033[1;31m╔══════════════╗')
	print('                     ║Invalid Option║')
	print('                     ╚══════════════╝')
	time.sleep(.7) # Wait
################################################################################################################


################################################################################################################
#                                        START THE MAIN FUNCTION/SCRIPT                                        #
################################################################################################################
Main()