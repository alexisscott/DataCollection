
import csv
import dvrk 
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
                p = dvrk.psm('PSMR3')
                p.home()
                import PyKDL
                p.dmove(PyKDL.Vector(0.0, 0.0005, 0.0))
                
            #Test point for information

            elif choice == 2:
                weight = input('Weight')
                displace=input('Displacement')
                force = weight*9.8
                joint_position = p.get_current_position()
                effort = p.get_current_joint_effort()
                print(force) 

                #Save/Write to CSV file
                csv_file_name = 'csv_testing1.csv'
                print "Values will be saved in", csv_file_name 
                f = open(csv_file_name,'a')
                writer = csv.writer(f)
                writer.writerow([force,displace,joint_position,effort])
                f.close()
           
            #Close Program
            elif choice == 0:
                done = True
            else: 
                print 'Error'

a = force_testing()
a.run()

      
   
