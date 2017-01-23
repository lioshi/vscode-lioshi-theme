a = 10
b = a +
        10
c = [ 5, 4, 
        10 ]
d = [ a ] \
        + c
print "#{a} #{b} [", c.join(" "), "] [", d.join(" "), "]\n";

for i in (1..10)
    rno = rand(100) + 1
    msg = case rno
        when 42: "The ultimate result."
        when 1..10: "Way too small."
        when 11..15,19,27: "Sorry, too small"
        when 80..99: "Way to large"
        when 100:
                print "TOPS\n"
                "Really way too large"
        else "Just wrong"
    end
    print "Result: ", rno, ": ", msg, "\n"
end

print "Triangle height: "
h = gets.to_f;
print "Triangle width: "
w = gets.to_f;
area = 0.5*h*w
print "Triangle height ", h, " width ", w, " has area ", area, "\n"

# See how it works.
(rand(4) + 2).times {
    a = rand(300)
    print a,"^2 = ", sqr(a), "\n"
}
print "\n"