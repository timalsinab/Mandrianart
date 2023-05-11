#include "CTurtle.hpp"   //This brings in the CTurtle library for use
#include <iostream> //for input & output
#include <random> //needed for Getrandom
#include <chrono> //needed for Getrandom's seed
namespace ct = cturtle;  //This makes it possible to use the CTurtle commands using ct::
using namespace std;

class Getrandom {
	/** Uses <random> and <chrono> from C++11 to return a random integer in range [1..size] */
public:
	Getrandom(int size) {
		auto seed = chrono::system_clock::now().time_since_epoch().count(); //gets a new seed for the randomness
		default_random_engine generator(seed);			//seeds our randomness
		uniform_int_distribution<int> intdist(1, size); //a distibution to make each in-range integer equally likely
		self_rand_int_ = intdist(generator);			//generates the randme number
	}
	int roll() {
		return self_rand_int_;
	}
private:
	int self_rand_int_;
};


class MondrianArt {

public:
	// Constructor of the class MandarianArt
	MondrianArt() {
		  //an array that contains that list of color
	}

	void setup_turtle(ct::Turtle& rt) {
		// method that draws the base rectangle i.e. biggest rectangle

		rt.penup();
		rt.goTo(-400, 300);
		rt.pendown();
		rt.forward(800);
		rt.right(90);
		rt.forward(600);
		rt.right(90);
		rt.forward(800);
		rt.right(90);
		rt.forward(600);
		rt.speed(0);
		rt.speed(ct::TS_FASTEST);

	}

	void mondrian(ct::Point a, int width, int height, ct::Turtle& rt, int base_case, ct::Color colors[]) {// method that draws the mondrian art
		
		
		if (width < base_case && height < base_case) {// base case because I want the turtle to stop when the width is less than or equal to 30
			return;
		}

		float w_buff = (0.25 * width); //get area around the edges of the square where we don't want our split point to be
		float h_buff = (0.25 * height);

		Getrandom newrandom((width - w_buff * 2) + 1); //get the random point for the rectangle to split
		Getrandom newrandom2((height - h_buff * 2) + 1); // do the same but for horizontal splits
		int randomwidth = w_buff + (newrandom.roll()); // split should be the distance from the origin that the split should be placed
		int randomheight = h_buff + (newrandom2.roll());
		
		Getrandom rand(6);
		rt.fillcolor((colors[rand.roll() - 1]));
		rt.goTo(a);
		rt.pendown();
		rt.begin_fill();
		rt.right(90);
		rt.forward(width);
		rt.right(90);
		rt.forward(height);
		rt.right(90);
		rt.forward(width);
		rt.right(90);
		rt.forward(height);
		rt.end_fill();
		rt.penup();
		
	

		if (width > 400 && height > 300) {     // when the width is half of the intial canvas size and height is half of the intial canvas size then split it in four rectangle
			mondrian({ a.x,a.y }, randomwidth, randomheight, rt, base_case,colors);          // top left
			mondrian({ a.x + randomwidth, a.y }, width - randomwidth, randomheight, rt, base_case,colors);  // top right
			mondrian({ a.x + randomwidth, a.y - randomheight }, width - randomwidth, height - randomheight, rt, base_case,colors);   // bottom right
			mondrian({ a.x, a.y - randomheight }, randomwidth, height - randomheight, rt, base_case,colors);  // bottom left
		}
		else if (height > 300) {
			mondrian({ a.x ,a.y }, width, randomheight, rt,base_case,colors);
			mondrian({ a.x,(a.y - randomheight) }, width, (height - randomheight), rt, base_case,colors); 
		}

		else if (width > 400) {
			mondrian({ a.x,a.y }, randomwidth, height, rt,base_case,colors);
			mondrian({ a.x + randomwidth,a.y }, (width - randomwidth), height, rt, base_case,colors);	
		}

		else if ((base_case < width && base_case < height)) {
			mondrian({ a.x,a.y }, randomwidth, randomheight, rt, base_case, colors);          // top left
			mondrian({ a.x + randomwidth, a.y }, width - randomwidth, randomheight, rt, base_case, colors);  // top right
			mondrian({ a.x + randomwidth, a.y - randomheight }, width - randomwidth, height - randomheight, rt, base_case, colors);   // bottom right
			mondrian({ a.x, a.y - randomheight }, randomwidth, height - randomheight, rt, base_case, colors);  // bottom left
		}

		else if (base_case < height) {
			mondrian({ a.x ,a.y }, width, randomheight, rt, base_case, colors);
			mondrian({ a.x,(a.y - randomheight) }, width, (height - randomheight), rt, base_case, colors);
		}

		else if (base_case < width) {
			mondrian({ a.x,a.y }, randomwidth, height, rt, base_case, colors);
			mondrian({ a.x + randomwidth,a.y }, (width - randomwidth), height, rt, base_case, colors);
		}
		
	}



	
private:
	string colorList[3];
};
int main() {
	int width = 800; // set the width of the rectangle to 
	int height = 600;  // set the height of the rectangle to 460
	ct::TurtleScreen(scr2);  // set the screen of the turtle 
	ct::Turtle myturtle(scr2);  // make the turtle
	scr2.tracer(1000, 10);
	int base_case = 15;
	MondrianArt MondrianArt2;   // make an instance of the MandrianArt
	MondrianArt2.setup_turtle(myturtle);  // make a turtle of instance of MandrainArt2
	int x = -400;
	int y = 300;
	ct::Point myPoints[] = { {x,y} };  // make points 
	ct::Color colors[] = { {0xD34A29}, {0x67CD54},{0xF9D913}, {0x9C9C9C}, {0x33231F}, {0x95E888} };
	MondrianArt2.mondrian(myPoints[0],width,height, myturtle,base_case,colors);  // call the method to draw the mondrian art
	scr2.exitonclick();
	return 0; 
}

