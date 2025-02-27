async function analyzeProducts(apiUrl, projectID) {
    try {
        const response = await fetch(apiUrl, {
            method: "GET",
            headers: { projectID }
        });
        if (!response.ok) {
            return {};
        }
        const result = await response.json();
        const products = result.data;
        const grouped = {
            "0-500": null,
            "501-1000": null,
            "1001-1500": null
        };
        const ranges = [
            { key: "0-500", min: 0, max: 500 },
            { key: "501-1000", min: 501, max: 1000 },
            { key: "1001-1500", min: 1001, max: 1500 }
        ];
        ranges.forEach(range => {
            const filtered = products.filter(product =>
                product.price >= range.min && product.price <= range.max
            );
            if (filtered.length > 0) {
                grouped[range.key] = filtered.reduce((best, current) =>
                    current.ratings > (best && best.ratings || 0) ? current : best, null
                );
            }
        });
        return Object.fromEntries(
            Object.entries(grouped).map(([key, value]) => [
                key,
                value ? { name: value.name, price: value.price, ratings: value.ratings } : null
            ])
        );
    } catch (error) {
        return {};
    }
}
