class Shape {
    /**
     * @return {Shape}
     */
    clone(): Shape {
        return new Shape();
    }

    getLength(): number {
        throw new Error("Not implemented");
    }

    getWidth(): number {
        throw new Error("Not implemented");
    }

    getHeight(): number {
        throw new Error("Not implemented");
    }
}

/**
 * @param {number} width
 * @param {number} height
 * @return {Rectangle}
 */
class Rectangle extends Shape {
    width: number;
    height: number;

    constructor(width, height) {
        super();
        this.width = width;
        this.height = height;
    }

    /**
     * @return {number}
     */
    getWidth(): number {
        return this.width;
    }

    /**
     * @return {number}
     */
    getHeight(): number {
        return this.height;
    }

    /**
     * @return {Shape}
     */
    clone(): Shape {
        return new Rectangle(this.width, this.height);
    }
}

/**
 * @param {number} length
 * @return {Square}
 */
class Square extends Shape {
    length: number;

    constructor(length) {
        super();
        this.length = length;
    }

    /**
     * @return {number}
     */
    getLength(): number {
        return this.length;
    }

    /**
     * @return {Shape}
     */
    clone(): Shape {
        return new Square(this.length);
    }
}

class Test {
    /**
     * @param {Shape[]} shapes
     * @return {Shape[]}
     */
    cloneShapes(shapes: Shape[]): Shape[] {
        let ss: Shape[] = [];

        for (let s of shapes) {
            ss.push(s.clone());
        }

        return ss;
    }
}
