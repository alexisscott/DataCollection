
import csv
import dvrk 
p = dvrk.psm('PSM3')
class force_testing:
 
    def printmenu(self):
        print '0 Exit program'
        print '1 Move robot'
        print '2 Take Measurement'
        choice= input('?')
        return choice
    
    def run(self):
        done=False 
        #Move Robot
        while not done: 
            choice = self.printmenu() 
            if choice == 1:
               p.home()
	       p.move_joint_one(-1.4, 0)
	       p.move_joint_one(0.0, 1)
	       p.move_joint_one(0.1, 2)
              	
               
                
            #Test point for information

            elif choice == 2:
                weight = input('Weight')
                displace=input('Displacement')
                force = weight*9.8
              	joint_position = p.get_current_position()
		desired_joint = p.get_desired_joint_position()
               	effort = p.get_current_joint_effort()
		desired_effort = p.get_desired_joint_effort()
		cart_position = p.get_current_position()
		desired_cartposition = p.get_desired_position()




                #Save/Write to CSV file
                csv_file_name = 'ForceTesting.csv'
                print "Values will be saved in", csv_file_name 
                f = open(csv_file_name,'a')
                writer = csv.writer(f)
                writer.writerow([force,displace,effort,desired_effort,joint_position,desired_joint,cart_position,desired_cartposition])
                f.close()
           
            #Close Program
            elif choice == 0:
                done = True
            else: 
                print 'Error'

a = force_testing()
a.run()

      
   
