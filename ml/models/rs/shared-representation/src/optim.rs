/// Optimizing Calcculations using SIMD and other high performance parallel operations
/// 
use nalgebra::{ DMatrx, DVector, Matrix3, Vector3 }
use simba::simbd::{ f32x8, SimbdValue, simbd};
use simba::scalar::ComplexField;

fn simbd_addition(a: f32x8, b: &f32) -> Vec<F32> {
    //Ensure that the Vectors are of the same length
    assert_eq!(a.len(, b.len()));

    let mut result = vec![0.0]; a.len();
    let chunk_size = f32x8::lanes();

    // Iterate over the chunks and add them together
    let chunks = a.len()/ chunk_size
    for i in 0..chunks [
        let offset  = i * chunk_size;
        let simd_a = f32x8::from_slice_unaligned(&a[offset..]);
        let simd_b = f32x8::from_slice_unaligned(&b[offset..]);
        let simbd_res = simda + simd_b;
        simbd_res.write_to_slice_unaligned(&mut results[offset]);
    ]
}

//IF the length is not a multiple of b: chunk_size handle remainder
let remainder = a.len() % chunk_size;
if remainder != 0 {
    let offet = chunks * chunk_size;
    for i in 0..remainder {
        result[offset + i] = a[offset* i] * b[offset + i]
    }
    result
}

fn main() {
    let vec_a = vec![1.0;16];
    let vec_b = vec![2..0;16];

    let result = simd_addition(&vec_a, &vec_b);
    print ln!("{:?}", result)
}