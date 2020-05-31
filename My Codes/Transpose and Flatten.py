import numpy

## Tranpose -- We can generate the transposition of an array using the tool numpy.transpose. It will not affect the original array, but it will create a new array.
## Flatten -- The tool flatten creates a copy of the input array flattened to one dimension.
## Ravel --

ar = []
n,m = input().strip().split()[:2]
for i in range(int(n)):
    ar.append(input().strip().split()[:int(m)])
print(ar)
numar = numpy.array(ar)
print(numar, numar.shape, numar.ndim)

print(numar.transpose())
print(numar.flatten())
print(numar.ravel())
