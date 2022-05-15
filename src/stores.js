import { writable } from 'svelte/store';

export const array = writable([]);
export const predictions = writable({});
export const showResults = writable(false);
