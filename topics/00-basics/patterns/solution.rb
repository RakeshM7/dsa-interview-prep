## https://takeuforward.org/strivers-a2z-dsa-course/must-do-pattern-problems-before-starting-dsa
class Patterns
    def user_input
        puts("Enter the number of rows: ")
        count = gets.chomp.to_i
        puts "Entered value : #{count}"
        return count
    end
    def pattern_1
        '''
            * * * *
            * * * *
            * * * *
            * * * *
        '''
        count = user_input
        for i in 1..count do
            for j in 1..count do
                print "*"
            end
            print "\n"
        end
    end

    def pattern_2
        '''
            *
            * *
            * * *
            * * * *
        '''
        count = user_input
        for i in 1..count do
            for j in 1..i do
                print '*'
            end
            print "\n"
        end
    end

    def pattern_3
        '''
            * * * *
            * * *
            * *
            *
        '''

        count = user_input
        for i in 1..count do
            for j in 1..count+1-i do
                print "*"
            end
            print "\n"
        end
    end

    def pattern_4
        '''
            1
            1 2
            1 2 3
            1 2 3 4
        '''
        count = user_input
        for i in 1..count do
            for j in 1..i do
                print j
            end
            print "\n"
        end
    end

    def pattern_5
        '''
            *
           ***
          *****
         *******
        '''
        count = user_input
        j_last = 2 * count
        for i in 0..count-1 do
            for j in 0...count-i-1 do
               print " "
            end
            for j in 0...2*i+1 do
                print "*"
            end
            for j in 0...count-i-1 do
                print " "
            end
            print "\n"
        end
    end

    def pattern_6
        '''
        1
        22
        333
        4444
        55555
        '''

        count = user_input
        for i in 0..count do
            for j in 0..i do
                print i + 1
            end
            print "\n"
        end
    end

    def pattern_7
        '''
        12345
        1234
        123
        12
        1
        '''
        count = user_input
        for i in 0..count-1 do
            for j in 0..count-1-i do
                print j+1
            end
            print "\n"
        end
    end

    def pattern_8
        '''
            *********
             *******
              *****
               ***
                *
        [no_of_spaces, no_of_stars, no_of_spaces]
        [0,9,0] -> 2*count - 1 - 0
        [1,7,1] -> 2*count - 1 - 2
        [2,5,2] -> 2*count - 1 - 4
        [3,3,3] -> 2*count - 1 - 6
        [4,1,4] -> 2*count - 1 - 8
        '''
        count = user_input
        for i in 0..count-1 do
            for j in 0..i do
                print " "
            end
            for j in 0..(2*count - 1 - 2*i)-1 do
                print "*"
            end
            for j in 0..i do
                print " "
            end
            print "\n"
        end
    end

    def pattern_9
        ''' 
            *
           ***
          *****
         *******
        *********
         *******
          *****
           ***
            *
        n = 5
        [4,1,4]
        [3,3,3]
        [2,5,2]
        [1,7,1]
        [0,9,0]
        [0,9,0]
        '''
        count = user_input
        for i in 0..count-1 do
            for j in 0..count-1-i do
                print " "
            end
            for j in 0..(2*i) do
                print "*"
            end
            for j in 0..count-1-i do
                print " "
            end
            print "\n"
        end
        for i in 1..count-1 do
            for j in 0..i do
                print " "
            end
            for j in 0..2*(count - i - 1) do
                print "*"
            end
            for j in 0..i do
                print " "
            end
            print "\n"
        end
        '''
        [0,7,0]
        [1,5,1]
        [2,3,2]
        [3,1,1]
        '''
        
    end

    def pattern_10
        '''
        *
        **
        ***
        ****
        *****
        ****
        ***
        **
        *

        n = 5
        [1,4]
        [2,3]
        [3,2]
        [2,1]
        [1,0]
        '''

        count = user_input
        
        for i in 0...count-1 do
            for j in 0..i do
                print "*"
            end
            print "\n"
        end
        for i in 0...count do
            for j in 0..count-i-1 do
                print "*"
            end
            print "\n"
        end
    end

    def pattern_11
        '''
        1
        01
        101
        0101
        10101
        '''
        count = user_input
        for i in 0..count-1 do
            for j in 0..i do
                print (i+j+1) % 2
            end
            print "\n"
        end
    end

    def pattern_12
        '''
        1      1
        12    21
        123  321
        12344321
        [1,6,1]
        [2,4,2]
        [3,2,3]
        [4,0,4]
        '''

        count = user_input
        for i in 0..count-1 do
            for j in 0..i do
                print j+1
            end
            for j in 1..2*(count-1-i) do
                print " "
            end
            for j in 0..i do
                print i-j+1
            end
            print "\n"
        end
    end

    def pattern_13
        '''
        1
        23
        456
        78910
        1112131415
        '''
        count = user_input
        counter = 1
        for i in 0..count-1 do
            for j in 0..i do
                print counter
                counter+=1
            end
            print "\n"
        end
    end

    def pattern_14
        '''
            A
            AB
            ABC
            ABCD
            ABCDE
        '''
        count = user_input
        for i in 0..count-1 do
            for j in 0..i do
                print (j+65).chr
            end
            print "\n"
        end
    end

    def pattern_15
        '''
        ABCDE
        ABCD
        ABC
        AB
        A
        '''
        count = user_input
        for i in 0..count-1 do
            for j in 0..(count-1-i) do
                print (j+65).chr
            end
            print "\n"
        end
    end

    def pattern_16
        '''
        A
        BB
        CCC
        DDDD
        EEEEE
        '''

        count = user_input
        for i in 0..count-1 do
            for j in 0..i do
                print (i+65).chr
            end
            print "\n"
        end
    end
end


patterns_obj = Patterns.new
puts "Enter the pattern number: "
pattern_number = gets.chomp
puts "Entered value : #{pattern_number}"
# begin
    patterns_obj.send("pattern_#{pattern_number}")
# rescue => e
#     print "Eexception : #{e}"
#     # puts "Pattern not available. Request a valid pattern from the following list: #{Patterns.methods}"
# end
