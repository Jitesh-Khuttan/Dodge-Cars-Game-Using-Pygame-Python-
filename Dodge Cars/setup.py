import cx_Freeze 

executables = [cx_Freeze.Executable("Dodge_Cars_main.py")]

cx_Freeze.setup(name="Dodge Cars",options={"build_exe": {"packages":["pygame"],
                                                         "include_files":["BLUECAR.png","Bugatti.png","car.png","caropp1.png","caropp2.png","caropp3.png",
                                                                                                "explosion.gif","font.ttf","gameover.png","hiscore.txt","road1.jpg",
                                                                                                "longtree1.jpg","longtree2.jpg","shot.wav","gamemusic.mp3","GameIcon.png"
                                                                                                
                                                                                        ]}},
executables = executables)
