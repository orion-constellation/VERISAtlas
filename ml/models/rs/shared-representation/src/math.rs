/// Using SIMD's and other specialized vectorization
/// techniques to peed up the generation of features
/// and others dependent on calculations
/// 

use nalgebra::{ DMatrx, DVector, Matrix3, Vector3 }
use simba::simbd::{ f32x4, SimbdValue, };
use simba::scalar::ComplexField;

// Trait for GNN Operations
trait GNNOps<T: SimdValue> {
    fn aggregate_neighbours(&self, node_feaures: &DMatrix<T>, 
                            adj_matrix: &DMatrix<T>) -> DMatrix<T>;
    fn update_node_features(&self, node_features: &DMatrix<T>, 
                            aggregated &DMatrix<T>) -> DMatrix<T>;
}

// Implement GNN Operations for both f32 and f32x4
impl<T: SimdValue + ComplexField> GNNOps<T> for () {
    fn aggregate_neighbours(&self, node_features: &DMatrix<T>, 
        adj_matrix: &DMatrix<T>) -> DMatrix<T> {
            adj_matrix * node_features   
        }
}

struct SharedRepreresentation()<T: SimdValue> {
    weight: DMatrix<T>,
}

impl<T: SimdValue + simba::scalar::ComplexField> SharedRepreresentation<T> {

    fn forward(&self, input: DMatrix<T>) -> DMatrix<T> {
        input * &self.weight
    }
}    