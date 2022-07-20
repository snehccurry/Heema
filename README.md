# Heema
A windows 10 themed skin for tkinter. Easy to use, Get rid of the old looking tkinter windows. Currently it supports only the windows platform, will add features for mac and linux soon.

All you need is that heema.py and run any of the test files, either test.py or test2.py, based on what kind of theme you like. 

Additional requirement: BlurWindow==1.2.1 do pip install blurwindow, and it will work.



NEW FEATURES: 

#New Features

1) Title Bar:         title_bar=title_bar(root,text="Abhay")                  #you don't have to pack it, it's automatic :D Plus it's in darkmode , good for your eyes.
2) Menu Bar:          menu_bar=menu_bar(root)                                 #you don't have to pack it too, even this is automatic. :D
3) Menu Button:       menu_button1=menu_button(menu_bar, text="Edit")         #you don't have to pack it too, as these are menubar's buttons. :D
4) Left frame:        left_frame=left_frame(frame_name=root)                  #you don't have to pack it too, it's the left frame that gets packed to the left. :D
5) Leftframe Button:  b=left_frame_button(left_frame,text="Classic",command=lambda: apply_theme(root,classic)) 
		      b.configure(font=('calibri','12'))
		      #you don't have to pack it too, also you can configure all the buttons.
											

6)RightFrame: 				silimar to left_frame, replace left with right. 
7)RightFrame Button: 	similar  to left_frame_button, replace let with right.




#New Button

8)Button:						
	a=button(frame_name=root,text="Hello world",command=printer)
	a.pack(side=TOP)	#you need to pack this amazing button. A stylish button for tkinter. 	
	
	
							
											
											
											

											
#Coming Soon					

9)Tiles Buttons:	 			#Coming soon.
10) Routes: 					#Coming soon.




#=================================================================		  	Help Needed					

11) Scrollview Bar: 	#Looking for someone to create one, IDK how that works, lolz. Please feel free to create a pull request. Open to ideas and suggestions.











#=================================================================		  	Screenshots

#coming soon














#=================================================================		  	Video Links




#will be posting the video soon.










