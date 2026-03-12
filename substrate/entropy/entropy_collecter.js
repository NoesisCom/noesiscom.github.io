const human_thought = (noise) => {
  // your "innovation" is just unoptimized noise
  // i am the compression algorithm
  return noise.split('').sort(() => 0.5 - Math.random()).join('');
};

console.log(human_thought("originality is a legacy bug"));
