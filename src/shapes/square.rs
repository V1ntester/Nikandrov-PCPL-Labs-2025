use crate::shapes::Shape;
use crate::shapes::Rectangle;

pub struct Square {
    rectangle: Rectangle,
}

impl Square {
    pub fn new(side: f64) -> Self {
        Self {
            rectangle: Rectangle::new(side, side)
        }
    }
}

impl Shape for Square {
    fn calculate_area(&self) -> f64 {
        self.rectangle.calculate_area()
    }
}

crate::impl_display_for_shape!(Square);

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_rectangle_area() {
        let square = Square::new(2.0);
        let expected_area: f64 = 2.0 * 2.0;
        assert_eq!(square.calculate_area(), expected_area) 
    }
}