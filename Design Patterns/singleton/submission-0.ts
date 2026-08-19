class Singleton {
    static instance: string = "";
    /**
     * In JavaScript consider this method as the 'getInstance'
     */
    constructor() {
    }

    /**
     * @return {string}
     */
    getValue(): string {
        return Singleton.instance;
    }

    /**
     * @param {string} value
     * @return {void}
     */
    setValue(value: string): void {
        Singleton.instance = value;
    }
}
