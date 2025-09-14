use std::f64::consts::PI;
use crate::shapes::Shape;

pub struct Circle {
    radius: f64,
}

impl Circle {
    pub fn new(radius: f64) -> Self {
        Self { radius }
    }
}

impl Shape for Circle {
    fn calculate_area(&self) -> f64 {
        PI * self.radius * self.radius
    }
}

crate::impl_display_for_shape!(Circle);

#[cfg(test)]
mod tests {
    use std::f64::consts::PI;
    use super::*;

    #[test]
    fn test_circle_area() {
        let circle = Circle::new(3.0);
        let expected_area: f64 = PI * 3.0 * 3.0;
        assert!((circle.calculate_area() - expected_area).abs() < f64::EPSILON) 
    }
}