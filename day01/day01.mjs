import * as fs from 'fs/promises';

const calc1 = (readings) => {
    return readings.reduce(({ lastRead, count }, curRead) => {
        if (curRead > lastRead) {
            return { lastRead: curRead, count: count + 1 }
        }
        return { lastRead: curRead, count }
    }, { lastRead: Number.MAX_VALUE, count: 0 });
}

const sum = (arr) => {
    return arr.reduce((a, b) => a + b, 0);
}

const calc2 = (readings) => {
    let count = 0;
    for (let i = 1; i < readings.length - 2; i++) {
        const window1 = readings.slice(i - 1, i + 2);
        const window2 = readings.slice(i, i + 3);
        if (sum(window2) > sum(window1)) {
            count++;
        }
    }
    return count
}

const run = async (calcFunc) => {
    const fh = await fs.open('input.txt', 'r');
    const { buffer } = await fh.read();
    await fh.close();

    const readings = buffer
        .toString()
        .split("\n")
        .filter(l => l)
        .map(l => parseInt(l));

    return await calcFunc(readings)
}

(async () => {
    const { count: part1 } = await run(calc1);
    console.log(`part 1: ${part1}`);
    const part2 = await run(calc2);
    console.log(`part 2: ${part2}`);
})();