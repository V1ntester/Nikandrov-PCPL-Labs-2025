use crate::shapes::Shape;

pub struct Rectangle {
    width: f64,
    height: f64,
}

impl Rectangle {
    pub fn new(width: f64, height: f64) -> Self {
        Self { width, height }
    }
}

impl Shape for Rectangle {
    fn calculate_area(&self) -> f64 {
        self.width * self.height
    }
}

crate::impl_display_for_shape!(Rectangle);

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_rectangle_area() {
        let rectangle = Rectangle::new(2.0, 4.0);
        let expected_area: f64 = 2.0 * 4.0;
        assert_eq!(rectangle.calculate_area(), expected_area) 
    }
}