-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 16, 2024 at 06:06 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `simgmpinformatika`
--

-- --------------------------------------------------------

--
-- Table structure for table `akun_login`
--

CREATE TABLE `akun_login` (
  `id` int(11) NOT NULL,
  `username` varchar(99) NOT NULL,
  `email` varchar(99) NOT NULL,
  `password` varchar(99) NOT NULL,
  `id_user` int(10) NOT NULL,
  `jenis_akun` varchar(100) NOT NULL
)

--
-- Dumping data for table `akun_login`
--

INSERT INTO `akun_login` (`id`, `username`, `email`, `password`, `id_user`, `jenis_akun`) VALUES
(1, 'admin', 'admin@admin.com', '12345', 1, 'admin'),
(2, 'ikramabdillah', 'muhmata52@guru.smp.belajar.id', 'abdillah123456', 2, 'guru'),
(3, 'alimuddin', 'alimuddin04@guru.smp.belajar.id', '123456', 3, 'kepsek'),
(4, 'pengawasmapel', 'informatika@pengawas.smp.belajar.id', '123456', 4, 'pengawas');

-- --------------------------------------------------------

--
-- Table structure for table `data_akun`
--

CREATE TABLE `data_akun` (
  `id` int(11) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `nip` bigint(50) NOT NULL,
  `alamat` varchar(100) NOT NULL,
  `nomor_hp` bigint(20) NOT NULL,
  `email_pribadi` varchar(100) NOT NULL,
  `email_pmm` varchar(100) NOT NULL,
  `pendidikan_terakhir` varchar(50) NOT NULL,
  `tempat_lahir` varchar(100) NOT NULL,
  `tanggal_lahir` date NOT NULL,
  `jenis_kepegawaian` varchar(100) NOT NULL,
  `nik` bigint(50) NOT NULL,
  `nuptk` bigint(50) NOT NULL,
  `sekolah` varchar(99) NOT NULL,
  `jenis_kelamin` varchar(90) NOT NULL,
  `gol_jab` varchar(99) NOT NULL
)

--
-- Dumping data for table `data_akun`
--

INSERT INTO `data_akun` (`id`, `nama`, `nip`, `alamat`, `nomor_hp`, `email_pribadi`, `email_pmm`, `pendidikan_terakhir`, `tempat_lahir`, `tanggal_lahir`, `jenis_kepegawaian`, `nik`, `nuptk`, `sekolah`, `jenis_kelamin`, `gol_jab`) VALUES
(1, 'admin aplikasi', 198012122001031003, 'Jl. Traktor 2 No. 10', 812345678910, 'admin@admin.com', 'admin@guru.id', 'S1', 'Ujung Pandang', '1995-12-25', 'PNS', 73101234567890, 1234567890, '1', 'Laki-laki', 'Penata Muda, III/A'),
(2, 'Muhammad Ikram Abdillah Mata, S.Pd.', 199512252019031002, 'Siloro Desa Mangilu Kec. Bungoro', 85398225280, 'ikram.abdillah@gmail.com', 'muhmata52@guru.smp.belajar.id', 'S1', 'Ujung Pandang', '1995-12-25', 'PNS', 7371102512950008, 6557773674130003, '3', 'Laki-laki', 'Penata Muda, III/a'),
(3, 'Drs. H. Alimuddin, M.Pd.', 196904041994121005, 'Pabbundukan, Pangkajene', 82190164473, 'alimuddin@gmail.com', 'alimuddin04@guru.smp.belajar.id', 'S2', 'Tondong', '0196-04-04', 'PNS', 7310100404690003, 628723007230092, '3', 'Laki-laki', 'Pembina Tk. 1, IV/c'),
(4, 'Pengawas Mata Pelajaran', 1972012020012002, 'Pangkajene', 812345678910, 'pengawasinformatika@gmail.com', 'informatika@pengawas.smp.belajar.id', 'S2', 'Pangkajene', '1972-01-20', 'PNS', 7310840190280002, 65799049200495, '0', 'Perempuan', 'Pembina Tk. 1, IV/c');

-- --------------------------------------------------------

--
-- Table structure for table `data_kepsek`
--

CREATE TABLE `data_kepsek` (
  `id` int(11) NOT NULL,
  `nama_kepsek` varchar(100) NOT NULL,
  `nip_kepsek` bigint(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `data_kepsek`
--

INSERT INTO `data_kepsek` (`id`, `nama_kepsek`, `nip_kepsek`) VALUES
(1, 'Kepala Sekolah Admin', 197012121992011001),
(2, 'Dr. Mansyur, S.Pd., M.Pd.', 197006041994011004),
(3, 'Drs. H. Alimuddin, M.Pd.', 196904041994121005),
(99, 'Dr. Sabrun Jamil, S.Pi., M.P.', 187506212004111001);

-- --------------------------------------------------------

--
-- Table structure for table `data_sekolah`
--

CREATE TABLE `data_sekolah` (
  `id` int(11) NOT NULL,
  `nama_sekolah` varchar(100) NOT NULL,
  `alamat_sekolah` varchar(100) NOT NULL,
  `npsn` int(50) NOT NULL,
  `kecamatan` varchar(99) NOT NULL,
  `kab_kota` varchar(99) NOT NULL,
  `kepsek` int(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `data_sekolah`
--

INSERT INTO `data_sekolah` (`id`, `nama_sekolah`, `alamat_sekolah`, `npsn`, `kecamatan`, `kab_kota`, `kepsek`) VALUES
(0, 'Dinas Pendidikan dan Kebudayaan Kab. Pangkep', 'Jl. Andi Mappe, Samalewa', 90617, 'Bungoro', 'Pangkajene dan Kepulauan', 99),
(1, 'SMP Negeri 1 Merdeka', 'Jl. Adil dan Makmur Nomor 1', 45010011, 'Merdeka', 'Belajar', 1),
(2, 'SMP Negeri 1 Pangkajene', 'Jl. Andi Mauraga, Tumampua', 40300630, 'Pangkajene', 'Pangkajene dan Kepulauan', 2),
(3, 'SMP Negeri 2 Pangkajene', 'Jl. Andi Mauraga No.4, Tumampua', 40300638, 'Pangkajene', 'Pangkajene dan Kepulauan', 3),
(4, 'SMP Negeri 3 Pangkajene', 'Jl. Kesejahteraan Mattoangin, Mappasaile', 69946492, 'Pangkajene', 'Pangkajene dan Kepulauan', 4),
(5, 'SMP Negeri 1 Minasatene', 'Jl. H. Fadeli Lurang, Biraeng', 40300629, 'Minasatene', 'Pangkajene dan Kepulauan', 5),
(6, 'SMP Negeri 2 Minasatene', 'Minasatene, Bonto Langkasa', 40300637, 'Minasatene', 'Pangkajene dan Kepulauan', 5),
(7, 'SMP Negeri 1 Bungoro', 'Jl. Poros Tonasa 2, Samalewa', 40300596, 'Bungoro', 'Pangkajene dan Kepulauan', 7),
(8, 'SMP Negeri 2 Bungoro', 'Jl. Sela, Mangilu', 40300634, 'Bungoro', 'Pangkajene dan Kepulauan', 8),
(9, 'SMP Negeri 3 Bungoro', 'Bontorannu, Boriappaka', 40300616, 'Bungoro', 'Pangkajene dan Kepulauan', 9),
(10, 'SMP Negeri 1 Labakkang', 'Bontowa', 40300597, 'Labakkang', 'Pangkajene dan Kepulauan', 10),
(11, 'SMP Negeri 2 Labakkang', 'Bara Batu, Taraweang', 40300635, 'Labakkang', 'Pangkajene dan Kepulauan', 11),
(12, 'SMP Negeri 3 Labakkang', 'Jl. Pundata Baji, Pundata Baji', 40300617, 'Labakkang', 'Pangkajene dan Kepulauan', 12),
(13, 'SMP Negeri 4 Satap Bungoro', 'Jl. Lakocci Bonto Tanga, Tabo-tabo', 40314462, 'Bungoro', 'Pangkajene dan Kepulauan', 13),
(14, 'SMP Negeri 3 Minasatene', 'Jl. Arung Kajuara, Kalabbirang', 40310350, 'Minasatene', 'Pangkajene dan Kepulauan', 14),
(15, 'SMP Negeri 1 Balocci', 'Jl. Pendidikan No. 8, Kassi', 40300595, 'Balocci', 'Pangkajene dan Kepulauan', 15),
(16, 'SMP Negeri 2 Balocci', 'Jl. Manunggal, Balleangin', 40300633, 'Balocci', 'Pangkajene dan Kepulauan', 16),
(17, 'SMP IT Showatul Is Ad', 'Jl. Poros Padang Lampe KM 3, Marang', 40314482, 'Marang', 'Pangkajene dan Kepulauan', 17),
(18, 'SMP Negeri 1 Liukang Tupabbiring', 'Pulau Balang Lompo, Mattiro Sompe', 40300613, 'Liukang Tupabbiring', 'Pangkajene dan Kepulauan', 18),
(19, 'SMP Negeri 8 Satap Liukang Tupabbiring', 'Pulau Balang Caddi, Mattiro Bintang', 40316762, 'Liukang Tupabbiring', 'Pangkajene dan Kepulauan', 19),
(20, 'SMP Negeri 3 Satap Liukang Tupabbiring', 'Pulau Pajenekang, Mattiro Deceng', 40314487, 'Liukang Tupabbiring', 'Pangkajene dan Kepulauan', 20),
(21, 'SMP IT Al-Hikmah Pangkajene', 'Jl. Andi Mauraga, Jagong', 70005009, 'Pangkajene', 'Pangkajene dan Kepulauan', 21);

-- --------------------------------------------------------

--
-- Table structure for table `perangkat_pembelajaran`
--

CREATE TABLE `perangkat_pembelajaran` (
  `id` int(11) NOT NULL,
  `judul` varchar(100) NOT NULL,
  `tingkatan` varchar(100) NOT NULL,
  `deskripsi` varchar(200) NOT NULL,
  `nama_file` varchar(100) NOT NULL,
  `tipe_file` varchar(100) NOT NULL,
  `size_file` bigint(60) NOT NULL,
  `id_user` int(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `pertemuan`
--

CREATE TABLE `pertemuan` (
  `id` int(11) NOT NULL,
  `pertemuan` int(12) NOT NULL,
  `tanggal` date NOT NULL,
  `lokasi` int(12) NOT NULL,
  `link` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pertemuan`
--

INSERT INTO `pertemuan` (`id`, `pertemuan`, `tanggal`, `lokasi`, `link`) VALUES
(1, 1, '2023-12-23', 3, 'http://www.zoom.com'),
(2, 2, '2023-12-30', 11, 'http://www.zoom.com'),
(3, 3, '2024-01-06', 5, 'http://www.zoom.com'),
(4, 4, '2024-01-13', 2, 'http://www.zoom.com'),
(5, 5, '2024-01-27', 4, 'http://www.zoom.com'),
(6, 6, '2024-02-03', 7, 'http://www.zoom.com'),
(7, 7, '2024-02-10', 9, 'http://www.zoom.com'),
(8, 8, '2024-02-24', 3, 'http://www.zoom.com');

-- --------------------------------------------------------

--
-- Table structure for table `praktik_baik`
--

CREATE TABLE `praktik_baik` (
  `id` int(11) NOT NULL,
  `judul_praktik` varchar(100) NOT NULL,
  `tingkatan` varchar(100) NOT NULL,
  `deskripsi` varchar(400) NOT NULL,
  `tanggal_praktik` date NOT NULL,
  `nama_file` varchar(100) NOT NULL,
  `tipe_file` varchar(100) NOT NULL,
  `size_file` bigint(20) NOT NULL,
  `id_user` bigint(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `praktik_baik`
--

INSERT INTO `praktik_baik` (`id`, `judul_praktik`, `tingkatan`, `deskripsi`, `tanggal_praktik`, `nama_file`, `tipe_file`, `size_file`, `id_user`) VALUES
(1, 'pembelajaran bilangan biner', 'Kelas 7', 'ini adalah contoh praktik baik yang memberikan contoh bagaimana menyajikan pelajaran informatika materi bilangan biner', '2024-01-23', 'biner.pdf', 'pdf', 15000, 1),
(4, 'Scratch', 'Kelas 8', 'Aplikasi Scratch memberikan dampak yang baik dalam pembelajaran. Scratch digunakan di sekolah sekolah di segala penjuru dunia sebagai media untuk mengenalkan pemrograman dasar ke anak-anak. Scratch membantu peserta didik untuk dapat belajar sambil bermain.', '2024-02-02', 'Tutorial JGE.pdf', 'pdf', 182176, 3);

-- --------------------------------------------------------

--
-- Table structure for table `supervisi`
--

CREATE TABLE `supervisi` (
  `id` int(11) NOT NULL,
  `id_user` int(12) NOT NULL,
  `semester` int(12) NOT NULL,
  `nama_file` varchar(100) NOT NULL,
  `waktu_pengajuan` date NOT NULL,
  `status_kepsek` int(12) NOT NULL,
  `status_pengawas` int(12) NOT NULL,
  `deskripsi_kepsek` varchar(200) NOT NULL,
  `deskripsi_pengawas` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `supervisi`
--

INSERT INTO `supervisi` (`id`, `id_user`, `semester`, `nama_file`, `waktu_pengajuan`, `status_kepsek`, `status_pengawas`, `deskripsi_kepsek`, `deskripsi_pengawas`) VALUES
(1, 2, 1, 'VII INFORMATIKA - SUSULAN.pdf', '2024-02-09', 1, 1, 'ok', 'Sudah sesuai'),
(2, 2, 2, 'Tutorial JGE.pdf', '2024-02-09', 2, 2, 'Lengkapi jurnal harian', 'Lengkapi instrumen penilaian');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `akun_login`
--
ALTER TABLE `akun_login`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `data_akun`
--
ALTER TABLE `data_akun`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `data_kepsek`
--
ALTER TABLE `data_kepsek`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `data_sekolah`
--
ALTER TABLE `data_sekolah`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `perangkat_pembelajaran`
--
ALTER TABLE `perangkat_pembelajaran`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `pertemuan`
--
ALTER TABLE `pertemuan`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `praktik_baik`
--
ALTER TABLE `praktik_baik`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `supervisi`
--
ALTER TABLE `supervisi`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `praktik_baik`
--
ALTER TABLE `praktik_baik`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `supervisi`
--
ALTER TABLE `supervisi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
