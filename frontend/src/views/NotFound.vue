<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <div class="text-center">
      <h1 class="text-5xl font-bold text-gray-900 mb-4">
        <i class="fas fa-exclamation-triangle" />
        Oops! Page not found
      </h1>
      <p class="text-xl text-gray-600 mb-8">
        The page you are looking for does not exist.
      </p>
      <router-link to="/" class="inline-block px-8 py-4 font-bold text-white bg-blue-500 rounded hover:bg-blue-600 transition-colors duration-300">Go to home page</router-link>
    </div>
  </div>
</template>