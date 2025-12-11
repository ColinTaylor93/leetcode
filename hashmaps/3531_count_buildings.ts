function countCoveredBuildings(n: number, buildings: number[][]): number {
    // Set for O(1) lookups
    const buildingSet = new Set<string>();

    const rows = new Map<number, number[]>();
    const cols = new Map<number, number[]>();

    for (const [x, y] of buildings) {
        buildingSet.add(`${x},${y}`);

        if (!rows.has(x)) rows.set(x, []);
        rows.get(x)!.push(y);

        if (!cols.has(y)) cols.set(y, []);
        cols.get(y)!.push(x);
    }

    // Sort lists for binary search
    for (const list of rows.values()) list.sort((a, b) => a - b);
    for (const list of cols.values()) list.sort((a, b) => a - b);

    let covered = 0;

    for (const [x, y] of buildings) {
        const rowList = rows.get(x)!;
        const colList = cols.get(y)!;

        const rowIndex = binarySearch(rowList, y);
        const colIndex = binarySearch(colList, x);

        const hasLeft = rowIndex > 0;
        const hasRight = rowIndex < rowList.length - 1;

        const hasAbove = colIndex > 0;
        const hasBelow = colIndex < colList.length - 1;

        if (hasLeft && hasRight && hasAbove && hasBelow) {
            covered++;
        }
    }

    return covered;
}

function binarySearch(arr: number[], target: number): number {
    let lo = 0, hi = arr.length - 1;
    while (lo <= hi) {
        const mid = (lo + hi) >> 1;
        if (arr[mid] === target) return mid;
        if (arr[mid] < target) lo = mid + 1;
        else hi = mid - 1;
    }
    return -1;
}