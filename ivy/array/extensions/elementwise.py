# global
import abc
from typing import Optional, Union

# local
import ivy


class ArrayWithElementWiseExtensions(abc.ABC):
    def sinc(self: ivy.Array, *, out: Optional[ivy.Array] = None) -> ivy.Array:
        """
        ivy.Array instance method variant of ivy.sinc. This method simply wraps the
        function, and so the docstring for ivy.sinc also applies to this method
        with minimal changes.

        Parameters
        ----------
        self
            input array whose elements are each expressed in radians. Should have a
            floating-point data type.
        out
            optional output array, for writing the result to. It must have a shape that
            the inputs broadcast to.

        Returns
        -------
        ret
            an array containing the sinc of each element in ``self``. The returned
            array must have a floating-point data type determined by
            :ref:`type-promotion`.

        Examples
        --------
        >>> x = ivy.array([0.5, 1.5, 2.5, 3.5])
        >>> y = x.sinc()
        >>> print(y)
        ivy.array([0.637,-0.212,0.127,-0.0909])
        """
        return ivy.sinc(self._data, out=out)

    def lcm(
        self: ivy.Array, x2: ivy.Array, *, out: Optional[ivy.Array] = None
    ) -> ivy.Array:
        """
        ivy.Array instance method variant of ivy.lcm. This method simply wraps the
        function, and so the docstring for ivy.lcm also applies to this method
        with minimal changes.

        Parameters
        ----------
        self
            first input array.
        x2
            second input array
        out
            optional output array, for writing the result to.

        Returns
        -------
        ret
            an array that includes the element-wise least common multiples
            of 'self' and x2

        Examples
        --------
        >>> x1=ivy.array([2, 3, 4])
        >>> x2=ivy.array([5, 8, 15])
        >>> x1.lcm(x2)
        ivy.array([10, 21, 60])
        """
        return ivy.lcm(self, x2, out=out)

    def fmod(
        self: ivy.Array,
        x2: ivy.Array,
        /,
        *,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        """ivy.Array instance method variant of ivy.fmod. This method simply
        wraps the function, and so the docstring for ivy.fmod also applies to
        this method with minimal changes.

        Parameters
        ----------
        self
        x1
            First input array.
        x2
            Second input array
        out
            optional output array, for writing the result to.

        Returns
        -------
        ret
            Array with element-wise remainder of divisions.

        Examples
        --------
        >>> x1 = ivy.array([2, 3, 4])
        >>> x2 = ivy.array([1, 5, 2])
        >>> x1.fmod(x2)
        ivy.array([ 0,  3,  0])

        >>> x1 = ivy.array([ivy.nan, 0, ivy.nan])
        >>> x2 = ivy.array([0, ivy.nan, ivy.nan])
        >>> x1.fmod(x2)
        ivy.array([ nan,  nan,  nan])
        """
        return ivy.fmod(self._data, x2, out=out)

    def fmax(
        self: ivy.Array,
        x2: ivy.Array,
        /,
        *,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        """ivy.Array instance method variant of ivy.fmax. This method simply
        wraps the function, and so the docstring for ivy.fmax also applies to
        this method with minimal changes.

        Parameters
        ----------
        self
        x1
            First input array.
        x2
            Second input array
        out
            optional output array, for writing the result to.

        Returns
        -------
        ret
            Array with element-wise maximums.

        Examples
        --------
        >>> x1 = ivy.array([2, 3, 4])
        >>> x2 = ivy.array([1, 5, 2])
        >>> ivy.fmax(x1, x2)
        ivy.array([ 2.,  5.,  4.])

        >>> x1 = ivy.array([ivy.nan, 0, ivy.nan])
        >>> x2 = ivy.array([0, ivy.nan, ivy.nan])
        >>> x1.fmax(x2)
        ivy.array([ 0,  0,  nan])
        """
        return ivy.fmax(self._data, x2, out=out)

    def trapz(
        self: ivy.Array,
        /,
        *,
        x: Optional[ivy.Array] = None,
        dx: Optional[float] = 1.0,
        axis: Optional[int] = -1,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        """ivy.Array instance method variant of ivy.trapz. This method simply
        wraps the function, and so the docstring for ivy.trapz also applies to
        this method with minimal changes.

        Parameters
        ----------
        self
            The array that should be integrated.
        x
            The sample points corresponding to the input array values.
            If x is None, the sample points are assumed to be evenly spaced
            dx apart. The default is None.
        dx
            The spacing between sample points when x is None. The default is 1.
        axis
            The axis along which to integrate.
        out
            optional output array, for writing the result to.

        Returns
        -------
        ret
            Definite integral of n-dimensional array as approximated along
            a single axis by the trapezoidal rule. If the input array is a
            1-dimensional array, then the result is a float. If n is greater
            than 1, then the result is an n-1 dimensional array.

        Examples
        --------
        >>> y = ivy.array([1, 2, 3])
        >>> ivy.trapz(y)
        4.0
        >>> y = ivy.array([1, 2, 3])
        >>> x = ivy.array([4, 6, 8])
        >>> ivy.trapz(y, x=x)
        8.0
        >>> y = ivy.array([1, 2, 3])
        >>> ivy.trapz(y, dx=2)
        8.0
        """
        return ivy.trapz(self._data, x=x, dx=dx, axis=axis, out=out)

    def float_power(
        self: Union[ivy.Array, float, list, tuple],
        x2: Union[ivy.Array, float, list, tuple],
        /,
        *,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        """ivy.Array instance method variant of ivy.float_power. This method simply
        wraps the function, and so the docstring for ivy.float_power also applies to
        this method with minimal changes.

        Parameters
        ----------
        self
            Array-like with elements to raise in power.
        x2
            Array-like of exponents. If x1.shape != x2.shape,
            they must be broadcastable to a common shape
            (which becomes the shape of the output).
        out
            optional output array, for writing the result to.

        Returns
        -------
        ret
            The bases in x1 raised to the exponents in x2.
            This is a scalar if both x1 and x2 are scalars

        Examples
        --------
        >>> x1 = ivy.array([1, 2, 3, 4, 5])
        >>> x1.float_power(3)
        ivy.array([1.,    8.,   27.,   64.,  125.])
        >>> x1 = ivy.array([1, 2, 3, 4, 5])
        >>> x2 = ivy.array([2, 3, 3, 2, 1])
        >>> x1.float_power(x2)
        ivy.array([1.,   8.,  27.,  16.,   5.])
        """
        return ivy.float_power(self._data, x2, out=out)

    def exp2(
        self: Union[ivy.Array, float, list, tuple],
        /,
        *,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        """ivy.Array instance method variant of ivy.exp2. This method simply
        wraps the function, and so the docstring for ivy.exp2 also applies to
        this method with minimal changes.

        Parameters
        ----------
        self
            Array-like input.
        out
            optional output array, for writing the result to.

        Returns
        -------
        ret
            Element-wise 2 to the power x. This is a scalar if x is a scalar.

        Examples
        --------
        >>> x = ivy.array([1, 2, 3])
        >>> x.exp2()
        ivy.array([2.,    4.,   8.])
        >>> x = [5, 6, 7]
        >>> x.exp2()
        ivy.array([32.,   64.,  128.])
        """
        return ivy.exp2(self._data, out=out)

    def nansum(
        self: ivy.Array,
        /,
        *,
        axis: Optional[Union[tuple, int]] = None,
        dtype: Optional[Union[ivy.Dtype, ivy.NativeDtype]] = None,
        keepdims: Optional[bool] = False,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Array:
        """
        ivy.Array instance method variant of ivy.nansum. This method simply
        wraps the function, and so the docstring for ivy.nansum also applies to
        this method with minimal changes.

        Parameters
        ----------
        self
            Input array.
        axis
            Axis or axes along which the sum is computed.
            The default is to compute the sum of the flattened array.
        dtype
            The type of the returned array and of the accumulator in
            which the elements are summed. By default, the dtype of input is used.
        keepdims
            If this is set to True, the axes which are reduced are left
            in the result as dimensions with size one.
        out
            Alternate output array in which to place the result.
            The default is None.

        Returns
        -------
        ret
            A new array holding the result is returned unless out is specified,
            in which it is returned.

        Examples
        --------
        >>> a = ivy.array([[ 2.1,  3.4,  ivy.nan], [ivy.nan, 2.4, 2.1]])
        >>> ivy.nansum(a)
        10.0
        >>> ivy.nansum(a, axis=0)
        ivy.array([2.1, 5.8, 2.1])
        >>> ivy.nansum(a, axis=1)
        ivy.array([5.5, 4.5])
        """
        return ivy.nansum(
            self._data, axis=axis, dtype=dtype, keepdims=keepdims, out=out
        )

    def gcd(
        self: Union[ivy.Array, int, list, tuple],
        x2: Union[ivy.Array, int, list, tuple],
        /,
        *,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        """ivy.Array instance method variant of ivy.gcd. This method simply
        wraps the function, and so the docstring for ivy.gcd also applies to
        this method with minimal changes.

        Parameters
        ----------
        self
            First array-like input.
        x2
            Second array-like input
        out
            optional output array, for writing the result to.

        Returns
        -------
        ret
            Element-wise gcd of |x1| and |x2|.

        Examples
        --------
        >>> x1 = ivy.array([1, 2, 3])
        >>> x2 = ivy.array([4, 5, 6])
        >>> x1.gcd(x2)
        ivy.array([1.,    1.,   3.])
        >>> x1 = ivy.array([1, 2, 3])
        >>> x1.gcd(10)
        ivy.array([1.,   2.,  1.])
        """
        return ivy.gcd(self._data, x2, out=out)

    def isposinf(
        self: Union[ivy.Array, float, list, tuple],
        /,
        *,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Array:
        """
        ivy.Array instance method variant of ivy.isposinf. This method simply
        wraps the function, and so the docstring for ivy.isposinf also applies to
        this method with minimal changes.
        
        Parameters
        ----------
        self
            Input array.
        out
            Alternate output array in which to place the result.
            The default is None.
        
        Returns
        -------
        ret
            Returns a boolean array with values True where 
            the corresponding element of the input is positive
            infinity and values False where the element of the
            input is not positive infinity.
        
        Examples
        --------
        >>> a = ivy.array([12.1, -ivy.inf, ivy.inf])
        >>> ivy.isposinf(a)
        ivy.array([False, False,  True])
        """
        return ivy.isposinf(self._data, out=out)

    def isneginf(
        self: Union[ivy.Array, float, list, tuple],
        /,
        *,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Array:
        """
        ivy.Array instance method variant of ivy.isneginf. This method simply
        wraps the function, and so the docstring for ivy.isneginf also applies to
        this method with minimal changes.
        
        Parameters
        ----------
        self
            Input array.
        out
            Alternate output array in which to place the result.
            The default is None.
        
        Returns
        -------
        ret
            Returns a boolean array with values True where 
            the corresponding element of the input is negative
            infinity and values False where the element of the
            input is not negative infinity.
        
        Examples
        --------
        >>> x = ivy.array([12.1, -ivy.inf, ivy.inf])
        >>> x.isneginf()
        ivy.array([False, True,  False])
        """
        return ivy.isneginf(self._data, out=out)
