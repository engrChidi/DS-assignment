#Python Assignments

#1. Division of the array inputs, element-wise:
import numpy as np
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Original array:")
print(x)
print("Division of the array inputs, element-wise:")
print(np.true_divide(x, 3))

#2. Largest integer smaller or equal to the division of the inputs
x = [1.0, 2.0, 3.0, 4.0]
print("Original array:")
print(x)
print("Largest integer smaller or equal to the division of the inputs:")
print(np.floor_divide(x, 1.5))

#3. print("First array elements raised to powers from second array, element-wise
x = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
print("Original array")
print(x)
print("First array elements raised to powers from second array, element-wise:")
print(np.power(x, 3))

#4. Element-wise remainder of division
x = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
print("Original array:")
print(x)
print("Element-wise remainder of division:", np.remainder(x, 5))

#5.Element-wise absolute value 
x = np.array([-10.2, 122.2, .20])
print("Original array:")
print(x)
print("Element-wise absolute value:", np.absolute(x))

#6. A NumPy program to get the element-wise remainder of an array of division.
x = np.round([1.23, 1.90, 2.40])
print(x)
x = np.round([0.32, .49, .62], decimals=1)
print(x)
x = np.round([.2, 1.8, 2.4, 4.1, 4.0])
print(x)

#7.Round elements of the array to the nearest integer 
x = np.array([-.7, -1.5, -1.7, 0.3, 1.5, 1.8, 2.0])
print("Original array:")
print(x)
x = np.rint(x)
print("Round elements of the array to the nearest integer:")
print(x)

#8. A NumPy program to get the floor, ceiling and truncated values of the elements of a numpy array.
x = np.array([-1.6, -1.5, -0.3, 0.1, 1.4, 1.8, 2.0])
print("Original array:")
print(x)
print("Floor values of the above array elements:")
print(np.floor(x))
print("Ceil values of the above array elements:")
print(np.ceil(x))
print("Truncated values of the above array elements:")
print(np.trunc(x))

#9. A NumPy program to add, subtract, multiply, divide arguments element-wise.
print("Add:")
print(np.add(2.0, 3.0))
print("Subtract:")
print(np.subtract(10.0, 13.0))
print("Multiply:")
print(np.multiply(2.0, 2.0))
print("Divide:")
print(np.divide(1.0, 4.0))

#10. a NumPy program to compute logarithm of the sum of exponentiations of the inputs, sum of exponentiations of the inputs in base-2. 
log1 = np.log(1e-50)
log2 = np.log(2.5e-50)
print("Logarithm of the sum of exponentiations:")
print(np.logaddexp(log1, log2))
print("Logarithm of the sum of exponentiations of the inputs in base-2:")
print(np.logaddexp2(log1, log2))