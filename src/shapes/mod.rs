mod circle;
mod rectangle;
mod square;

pub use circle::Circle;
pub use rectangle::Rectangle;
pub use square::Square;

#[macro_export]
macro_rules! impl_display_for_shape {
    ($type:ident) => {
        impl ::std::fmt::Display for $type {
            fn fmt(&self, formatter: &mut ::std::fmt::Formatter<'_>) -> ::std::fmt::Result {
                write!(
                    formatter,
                    "Shape: {}; Area {};",
                    stringify!($type),
                    self.calculate_area()
                )
            }
        }
    };
}

pub trait Shape {
    fn calculate_area(&self) -> f64;
}
