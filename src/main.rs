mod shapes;

use shapes::{Circle, Rectangle, Square};

fn main() {
    let circle = Circle::new(1.0);
    println!("{}", circle);

    let rectangle = Rectangle::new(2.0, 3.0);
    println!("{}", rectangle.to_string());

    let square = Square::new(2.0);
    println!("{}", square);
}